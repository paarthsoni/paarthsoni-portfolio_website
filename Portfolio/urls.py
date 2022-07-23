from django import views
from django.contrib import admin
from django.urls import path
from Portfolio import views
urlpatterns = [
    path('', views.index, name="home"),
]
