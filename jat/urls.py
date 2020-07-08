from django.urls import path
from . import views

app_name = 'jat'
urlpatterns = [
  path('', views.index, name='index'),
  path('new_app', views.new_app, name='new_app'),
  path('new_act', views.new_act, name='new_act'),
]