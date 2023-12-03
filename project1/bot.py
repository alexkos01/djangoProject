import asyncio
import logging
from asyncio import Lock
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token="")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

lock = Lock()

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Base = declarative_base()


class Users(Base):
    __tablename__ = 'project1_modelreg'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    email = Column(String)

    def __init__(self, a, b, c):
        self.login = a
        self.password = b
        self.email = c


Session = sessionmaker(bind=engine)
session = Session()


class States(StatesGroup):
    login = State()
    email = State()
    password = State()


class DataSales:
    dt_user = {}

user_but = ReplyKeyboardMarkup(resize_keyboard=True)
user_but.add(KeyboardButton(text='регистрация'), KeyboardButton(text='выход'))

@dp.message_handler(commands='start')
async def cmd_end(mes: types.Message):
    await mes.reply(f'{mes.from_user.first_name}, воспользуйтесь кнопками для дальнейших действий', reply_markup=user_but)


@dp.message_handler(text='выход')
async def exit_bot(mes: types.Message):
    user_inl1 = InlineKeyboardMarkup()
    user_inl1.add(InlineKeyboardButton('вернуться на сайт', url='http://127.0.0.1:8000/info/'))
    await mes.reply('выход', reply_markup=user_inl1)



@dp.message_handler(text='регистрация')
async def cmd_start(mes: types.Message):
    await mes.answer('введите логин')
    await States.login.set()


@dp.message_handler(state=States.login)
async def save_login(mes: types.Message, state: FSMContext):
    if len(mes.text) < 2:
        return await mes.answer('логин не может быть таким коротким')
    async with lock:
        DataSales.dt_user['login'] = mes.text
    await mes.answer('введите email')
    await States.email.set()


@dp.message_handler(state=States.email)
async def save_email(mes: types.Message, state: FSMContext):
    if '@' not in mes.text:
        return await mes.answer('в email отсутсвует @')
    async with lock:
        DataSales.dt_user['email'] = mes.text
    await mes.answer('введите пароль')
    await States.password.set()


@dp.message_handler(state=States.password)
async def save_password(mes: types.Message, state: FSMContext):
    if len(mes.text) < 5:
        return await mes.answer('пароль не может быть таким коротким')
    async with lock:
        DataSales.dt_user['password'] = mes.text
    await state.finish()
    await mes.answer('регистрация прошла успешна')
    session.add(Users(DataSales.dt_user["login"], DataSales.dt_user["password"], DataSales.dt_user["email"]))
    session.commit()



async def main():
    Base.metadata.create_all(engine)
    await dp.start_polling(bot)
