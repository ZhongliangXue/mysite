# Generated by Django 2.0.4 on 2018-04-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='up_time',
            field=models.DateTimeField(null=True),
        ),
    ]
