# Generated by Django 3.1.7 on 2021-04-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bujoapp', '0004_newprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
