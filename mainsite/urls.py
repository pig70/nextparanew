from django.urls import path
from . import views

urlpatterns = [
    path('stories/<slug:slug>/<int:pk>/', views.story, name='story'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registration-complete/', views.register_complete, name='registration_complete')
]
