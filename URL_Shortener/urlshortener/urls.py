from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name='home'),

	path('random_shortener/', views.random_shortener, name='random_shortener'),
	path('r/<urlid>/', views.random_shortened, name='random_shortened'),

	path('custom_shortener/', views.custom_shortener, name='custom_shortener'),
	path('c/<custom_name>/', views.custom_shortened, name='custom_shortened'),

]
