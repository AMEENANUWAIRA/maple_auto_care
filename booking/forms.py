from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'appointment_date', 'appointment_slot', 'services', 'contact_info', 'service_mode']
        widgets = {
            'appointment_date': forms.SelectDateWidget(),
            'appointment_slot': forms.Select(),
            'services': forms.CheckboxSelectMultiple(),
            'service_mode': forms.RadioSelect(),
        }
