# Generated by Django 3.1.7 on 2021-04-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bujoapp', '0010_thisweek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Today',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('TASK', 'task'), ('EVENT', 'event'), ('NOTE', 'note')], max_length=100)),
                ('task_description', models.CharField(max_length=100)),
            ],
        ),
    ]