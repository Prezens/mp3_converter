# Generated by Django 2.1.1 on 2019-06-26 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestvideo',
            name='date_request',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
