from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name if self.name else f"Customer {self.user.username}"

    # Override save method to ensure name is set if not provided
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username  # Set name as user's username if name is empty
        super(Customer, self).save(*args, **kwargs)


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('billing', 'Billing'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.name}"

# Signal to create a Customer object whenever a User is created
@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        print(f"User: {instance}")
        customer = Customer.objects.create(
            user=instance, 
            name=instance.username,
            email=instance.email,
        )
        customer.save()


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    if hasattr(instance, 'customer'):
        instance.customer.save()