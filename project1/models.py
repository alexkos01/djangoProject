from django.db import models


class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    img = models.ImageField(upload_to='imgs', default='')
