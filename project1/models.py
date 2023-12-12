from django.db import models


class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    img = models.ImageField(blank=True, upload_to='imgs')

    def __str__(self):
        return self.login
