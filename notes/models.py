from django.db import models


class Notes(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(max_length=300)

    class Meta:
        db_table = "notes"
