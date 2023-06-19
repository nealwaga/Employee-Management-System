from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='profile')
    image = CloudinaryField ('image')
    full_name = models.CharField (blank=False, max_length=100)
    email = models.EmailField (blank=False, max_length=100)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f'{self.user.username} - Profile'


    @receiver (post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver (post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()