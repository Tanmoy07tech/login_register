from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='homepage'),
    path('login', views.login),
    path('',views.home,name='homepage'),
    path('register',views.register),
    
   

]