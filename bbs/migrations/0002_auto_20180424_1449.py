# Generated by Django 2.0.4 on 2018-04-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='输入帖子标题', max_length=32),
        ),
    ]
