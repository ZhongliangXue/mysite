# Generated by Django 2.0.4 on 2018-04-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20180424_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]