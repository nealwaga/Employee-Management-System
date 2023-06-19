from django.urls import path
from . import views


#Create urls here

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pdf/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
]
