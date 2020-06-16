from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^register$', views.register, name="register"),
    url('^register_handle$', views.register_handle, name="register_handle"),
    url('^register_exist$', views.register_exist, name="register_exist"),
    url('^login$', views.login, name="register"),
    url('^login_handle$', views.login_handle, name="login_handle"),
    url('^info$', views.info, name="info"),
    url('^order$', views.order, name="order"),
    url('^site$', views.site, name="site"),
    url('^logout$', views.logout, name="logout"),
]