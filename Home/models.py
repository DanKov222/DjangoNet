from django.conf import settings
from django.db import models
from django.urls import reverse


class LocalPost(models.Model):
    """Публикация пользователя"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='post/', blank=True, default='post.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-date']


class Comments(models.Model):
    post = models.ForeignKey(LocalPost, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} -> {self.post}'

    class Meta:
        ordering = ['-date']


class Like(models.Model):
    """Лайки к LocalPost"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(LocalPost, on_delete=models.CASCADE, related_name='post')