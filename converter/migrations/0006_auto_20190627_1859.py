# Generated by Django 2.1.1 on 2019-06-27 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0005_auto_20190627_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestvideo',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 27, 18, 59, 5, 508789)),
        ),
    ]