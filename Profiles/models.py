from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Profile(AbstractUser):
    """Модель профиля"""
    avatar = models.ImageField(default='avatar.jpg', blank=True, upload_to='images/avatar/')
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    ages = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('login')

    class Meta(AbstractUser.Meta):
        pass


class FriendList(models.Model):
    """Список друзей"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')