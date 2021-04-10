from django.db import models

class ProfilePageModel(models.Model):
    nickname = models.CharField(max_length=100)