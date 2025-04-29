from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayServices, name="services"),
    path('create-service', views.createService, name="create-service"),
    path('get-service/<str:pk>/', views.getService, name="get-service"),
    path('update-service/<str:pk>/', views.updateService, name="update-service"),
    path('delete-service/<str:pk>/', views.deleteService, name="delete-service"),
]