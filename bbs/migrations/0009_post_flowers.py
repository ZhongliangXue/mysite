# Generated by Django 2.0.4 on 2018-04-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0008_auto_20180427_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='flowers',
            field=models.IntegerField(default=0),
        ),
    ]
