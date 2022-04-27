from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=20, unique=True)

