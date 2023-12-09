from django.db import models


# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='myapp/')


class Audios(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='myapp/')
