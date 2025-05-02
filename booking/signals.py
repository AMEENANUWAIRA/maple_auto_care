from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

@receiver(post_save, sender=Booking)
def booking_confirmation_mail(sender, instance, created, **kwargs):
    if created:
        booking = instance

        subject = "Maple Auto Care: Booking Confirmation"
        message = f"""
            Dear {booking.customer_name},

            Your booking (ID: {booking.id}) has been confirmed. 
            Here are your booking details:

            Appointment Date: {booking.appointment_date}
            Appointment Time: {booking.appointment_slot}

            Estimated Price: {booking.total_price}

            Thank you for choosing Maple Auto Care.
            We look forward to serving you!

            Best regards,
            Maple Auto Care Team
            """

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[booking.contact_info],
            fail_silently=False,
        )
