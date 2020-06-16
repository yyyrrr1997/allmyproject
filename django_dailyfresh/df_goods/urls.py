from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url('^$', views.index, name="index"),
    url('^list(\d+)_(\d+)_(\d+)$', views.goodlist, name="list"),
    url('^(\d+)$', views.gooddetail, name="detail"),
]
