# Generated by Django 2.0.4 on 2018-04-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_file_up_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='down_Pname',
            field=models.CharField(default='文件接收人', max_length=32),
        ),
        migrations.AddField(
            model_name='file',
            name='up_Pname',
            field=models.CharField(default='文件上传人', max_length=32),
        ),
    ]
