from django.contrib import admin
from bbs.models import post
from bbs.models import File
from bbs.models import BBS_user
from bbs.models import Category

class postAdmin(admin.ModelAdmin):
    list_display = ('title','flowers','writer','pub_time')
    list_filter = ('pub_time',)           #使用的是tuple，所以不要忘记加一个逗号
    search_fields = ('title','writer','content')
    ordering = ['pub_time','writer']

class FileAdmin(admin.ModelAdmin):
    list_display = ('filename','up_Pname','up_time')
    search_fields = ('filename',)

admin.site.register(post,postAdmin)
admin .site.register(File,FileAdmin)
admin.site.register(BBS_user)
admin.site.register(Category)

