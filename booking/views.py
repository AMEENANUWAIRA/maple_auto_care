from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from services.models import Service
from datetime import datetime, timedelta
from django.db.models import Count

def booking_home(request):
    return render(request, 'booking_home.html')

def new_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            # Prevent past date booking
            if booking.appointment_date < timezone.now().date():
                messages.error(request, "You cannot book an appointment for a past date.")
                return render(request, 'booking_form.html', {'form': form})

            # Triple booking prevention
            existing_bookings = Booking.objects.filter(
                appointment_date=booking.appointment_date,
                appointment_slot=booking.appointment_slot
            )
            if existing_bookings.count() >= 2:
                messages.error(request, "This slot already has 2 bookings. Please choose another slot.")
                return render(request, 'booking_form.html', {'form': form})

            # Validate contact info based on mode
            if booking.service_mode == 'email' and '@' not in booking.contact_info:
                messages.error(request, "Please provide a valid email address.")
                return render(request, 'booking_form.html', {'form': form})
            elif booking.service_mode == 'whatsapp' and not booking.contact_info.isdigit():
                messages.error(request, "Please provide a valid WhatsApp number.")
                return render(request, 'booking_form.html', {'form': form})

            # Calculate total price from selected services
            services = form.cleaned_data['services']
            total_price = sum(service.price for service in services)
            booking.total_price = total_price
            booking.save()
            form.save_m2m()

            request.session['booking_id'] = booking.id
            return redirect(reverse('confirmation:confirm_booking'))
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def modify_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect(reverse('confirmation:confirm_booking'))
    else:
        booking_id = request.GET.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
    return render(request, 'modify_booking.html', {'form': form})

def cancel_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            messages.success(request, "Booking cancelled successfully.")
            return redirect('services:home')
        except Booking.DoesNotExist:
            messages.error(request, "Booking ID not found.")
    return render(request, 'cancel_booking.html')
