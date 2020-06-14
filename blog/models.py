from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    publish_date = models.DateField(null=True, blank=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list')
