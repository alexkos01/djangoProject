# Generated by Django 4.2.7 on 2023-12-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0007_alter_modelreg_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelreg',
            name='img',
            field=models.ImageField(blank=True, upload_to='imgs'),
        ),
    ]
