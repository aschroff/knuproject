from django.urls import path
from . import views
from knu.dash_apps.finished_apps import simpleexample
from knu.dash_apps.finished_apps import location

app_name = 'knu'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('<int:value_id>/value/', views.value, name='value'),
    path('location', views.location, name='location'),
]