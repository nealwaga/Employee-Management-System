from django.urls import path
from . import views

#Create here
urlpatterns = [
    path('profile/', views.profile, name='profile')
    
]