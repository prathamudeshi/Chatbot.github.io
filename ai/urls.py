from django.contrib import admin
from django.urls import path,include
from ai import views

urlpatterns = [
    
    path('chat/', views.chat, name='chat'),
]