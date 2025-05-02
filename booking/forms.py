from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'appointment_date', 'appointment_slot', 'services', 'contact_info', 'service_mode']
        labels = {
            'customer_name': 'Name',
            'services': 'Select services',
            'contact_info': 'Contact number'
        }

        widgets = {
            'appointment_date': forms.SelectDateWidget(),
            'appointment_slot': forms.Select(),
            'services': forms.CheckboxSelectMultiple(),
            'service_mode': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input'}
            )


class DeleteBookingForm(forms.Form):
    booking_id = forms.CharField(
        label="Booking ID",
        max_length=30,  # Adjust length as needed
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., MAC-20250601-0900-001'
        })
    )

    def __init__(self, *args, **kwargs):
        super(DeleteBookingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

