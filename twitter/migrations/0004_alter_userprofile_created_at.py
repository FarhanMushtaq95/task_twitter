# Generated by Django 3.2 on 2021-05-01 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_alter_userprofile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 14, 16, 8, 696229)),
        ),
    ]
