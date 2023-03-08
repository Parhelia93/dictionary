from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, WordDetail, WordStage


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            django_user=instance
        )


@receiver(post_save, sender=WordDetail)
def create_word_stage(sender, instance, created, **kwargs):
    if created:
        WordStage.objects.create(
            word_stage=instance
        )
