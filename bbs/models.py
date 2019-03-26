from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class post(models.Model):                          #论坛帖子
    title = models.CharField(max_length=32,default='输入帖子标题')
    content = models.TextField(null=True)
    writer = models.CharField(max_length=32,default='帖子作者')
    pub_time = models.DateTimeField(null=True)
    view_account = models.IntegerField(default=0)
    summary = models.TextField(max_length=100,default='帖子概要')
    flowers = models.IntegerField(default=0)
    comment = models.TextField(max_length=100,default='输入评论')
    users_like = models.ManyToManyField(User, related_name="posts_like", blank=True)#文章点赞功能
    tags = TaggableManager()

    class Meta:
            verbose_name_plural = "帖子"



    def __str__(self): #添加一个方法，修改数据默认显示名称。在python2.7中为 __unicode__ 方法。
        return self.title


class File(models.Model):
    filename = models.CharField(max_length=30)
    file = models.FileField(upload_to='./upload') #默认把文件保存在mysite文件下的新建upload文件夹下
    up_Pname = models.CharField(max_length=32,default='文件上传人')
    down_Pname = models.CharField(max_length=32,default='文件接收人')
    up_time = models.DateTimeField(null=True)
    tags = TaggableManager()

    class Meta:
            verbose_name_plural = "文件"

    def __str__(self):
        return self.filename
                                                    #数据库中保存的是文件的路径，而没有保存文件

class BBS_user(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        signature = models.CharField(max_length=128, default='这个人太懒了，什么也没有留下...')

        class Meta:
            verbose_name_plural = "论坛版主"

        def __str__(self):
            return self.user

class Category(models.Model):
        name = models.CharField(max_length=32, unique=True)
        administrator = models.ForeignKey('BBS_user', on_delete=models.CASCADE)

        class Meta:
            verbose_name_plural = "论坛板块"







