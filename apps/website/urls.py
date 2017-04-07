from django.conf.urls import url, include
from . import views

app_name = "website"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about$', views.about, name="about"),
    url(r'^photography$', views.photography, name="photography"),
    url(r'^design$', views.design, name="design"),
    url(r'^blog$', views.blog, name="blog"),
    url(r'^contact$', views.contact, name="contact"),
]
