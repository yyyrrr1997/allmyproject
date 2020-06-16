from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url('^$', views.cartindex, name="cartindex"),
    url('^add(\d+)_(\d+)$', views.add, name="add"),
    url('^edit(\d+)_(\d+)$', views.edit, name="edit"),
    url('^delete(\d+)$', views.delete, name="delete"),

]

