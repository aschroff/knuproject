from django.urls import path
from . import views


app_name = 'member'
urlpatterns = [
    path('login_user', views.login_user, name='login'),
]