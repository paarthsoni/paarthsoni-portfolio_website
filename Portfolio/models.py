from email import message
from unicodedata import name
from django.db import models


class viewersmessage(models.Model):
    name = models.CharField(null=False, unique=False,
                            max_length=1024, default="NA")
    email = models.CharField(null=False, unique=False,
                             max_length=1024, default="NA")
    subject = models.CharField(
        null=False, unique=False, max_length=1024, default="NA")
    message = models.CharField(
        null=False, unique=False, max_length=5000, default="NA")

    def __str__(self):
        return self.name
