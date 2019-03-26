from django.urls import path,include,re_path
from . import views

urlpatterns = [
    re_path(r'^post_title/$', views.post_title),
    re_path(r'^post_title/(?P<post_id>[0-9]+)/$', views.post_page),
]