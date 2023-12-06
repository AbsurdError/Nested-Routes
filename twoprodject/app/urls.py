from app import views
from django.contrib import admin
from django.urls import path, re_path

product_patterns = [

]


urlpatterns = [
    path("set", views.set),
    path("get", views.get),
    path('', views.index),

]
