# from django.db import models

# from django.db import models
# from services.models import Service

# class Booking(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     customer_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     date = models.DateField()
#     time = models.TimeField()
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer_name} - {self.service.name} on {self.date} at {self.time}"

from django.db import models
from services.models import Service

class Booking(models.Model):
    SLOT_CHOICES = [
        ('09:00-10:00', '09:00-10:00'),
        ('10:00-11:00', '10:00-11:00'),
        ('11:00-12:00', '11:00-12:00'),
        ('12:00-13:00', '12:00-13:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
    ]

    SERVICE_MODE_CHOICES = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
    ]

    customer_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_slot = models.CharField(max_length=20, choices=SLOT_CHOICES)
    services = models.ManyToManyField(Service)
    contact_info = models.CharField(max_length=100)
    service_mode = models.CharField(max_length=10, choices=SERVICE_MODE_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.customer_name} - {self.appointment_date} @ {self.appointment_slot}"


