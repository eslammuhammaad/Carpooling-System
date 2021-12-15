from django.urls import path
from . import views
urlpatterns = [
    path('trip/', views.index, name='index'),
    path('', views.Home, name='Home'),
    path('track', views.track, name='track'),
    path('register', views.register, name='register'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('getRecommendations', views.getRecommendations,name='getRecommendations'),
]
