from django.db import models


class Profile(models.Model):
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

class NewProfile(models.Model):
    name = models.CharField(max_length=100)
