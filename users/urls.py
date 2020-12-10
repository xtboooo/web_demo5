from django.conf.urls import re_path
from users import views

urlpatterns = [
    re_path(r'^register/$', views.register),
    re_path(r'^login/$', views.login),
]
