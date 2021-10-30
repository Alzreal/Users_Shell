from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include ("User_app.urls")),
]
