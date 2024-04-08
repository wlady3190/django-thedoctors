from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from doctors.models import Doctor


@receiver(post_save, sender=Doctor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)


@receiver(post_save, sender=Doctor)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
