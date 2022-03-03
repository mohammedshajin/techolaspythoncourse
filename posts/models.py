from distutils.command.upload import upload
from email.mime import image
from tokenize import blank_re
from django.db import models

class Post(models.Model):
    caption = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to="media", blank=True, null=True)


    