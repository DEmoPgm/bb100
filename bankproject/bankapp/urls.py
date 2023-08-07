from . import views
from django.urls import path
app_name='bankapp'

urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('newpage',views.newpage,name='newpage'),
    path('logout',views.logout,name='logout'),



  ]