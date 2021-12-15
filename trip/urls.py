from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('getRecommendations', views.getRecommendations,name='getRecommendations'),
]
