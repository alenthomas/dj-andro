from django.conf.urls import include, url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^success', views.success, name='success'),
    ]
