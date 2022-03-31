from django.db import models

from users.models import Users


class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(max_length=200)


class Notes(models.Model):
    created = models.DateTimeField(default=True)
    updated = models.DateTimeField(default=True)
    text = models.TextField()
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)


