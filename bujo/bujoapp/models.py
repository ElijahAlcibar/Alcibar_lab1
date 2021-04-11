from django.db import models


class Profile(models.Model):
    picture = models.CharField(
        max_length=1000,
        default="https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg"
    )
    nickname = models.CharField(max_length=100, default="Your Nickname")
    bio = models.CharField(
        max_length=100, 
        default="A short description about yourself"
    )

class NewProfile(models.Model):
    name = models.CharField(max_length=100)
