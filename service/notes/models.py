from datetime import time
from django.db import models
# from users.models import Users
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    link_repo = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Notes(models.Model):
    time_created = models.DateTimeField(default=time())
    time_updated = models.DateTimeField(default=time())
    text = models.TextField()
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


