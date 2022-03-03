from unicodedata import name
from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("blog/<str:pk>/", views.blog, name="blog"),
    path("createpost/", views.createpost, name="createpost"),
    path('updatepost/<str:pk>/', views.updatepost, name="updatepost"),
    path('deletepost/<str:pk>/', views.deletepost, name="deletepost")
]