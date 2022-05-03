from django.contrib import admin
from django.urls import path,include
from .views import index
from katiya import views

urlpatterns = [
    path("", views.index),
]
