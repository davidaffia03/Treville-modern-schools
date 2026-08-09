from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
path('about-owner/', views.about_owner, name='about_owner'),]