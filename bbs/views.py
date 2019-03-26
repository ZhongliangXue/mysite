from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.template.context import RequestContext

from . import  models

def post_title(request):
    posts = models.post.objects.all()     #对应于sqlite中自动生成的主键id,pk的值决定了返回给前端的帖子是哪一个。   返回all时，posts默认为列表形式
    return render(request, 'bbs_post.html', {'posts':posts})

def post_page(request,post_id):
    post = models.post.objects.get(pk=post_id)
    return render(request,'post.html',{'post':post})

