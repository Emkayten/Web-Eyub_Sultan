from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    failed_attempts = models.IntegerField(default=0)
    lockout_until = models.DateTimeField(null=True, blank=True)
    sperre_count = models.IntegerField(default=0)
    
    roles = models.ManyToManyField(Role, blank=True)

    def is_locked_out(self):
        return self.lockout_until and timezone.now() < self.lockout_until

    def reset_attempts(self):
        self.failed_attempts = 0
        self.lockout_until = None
        self.save()

    def __str__(self):
        return f"{self.user.username} – {', '.join(role.name for role in self.roles.all())}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            from .models import UserProfile
            UserProfile.objects.create(user=instance)