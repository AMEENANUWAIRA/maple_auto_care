from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('new/', views.new_booking, name='new_booking'),
    path('modify/', views.modify_booking, name='modify_booking'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
]
