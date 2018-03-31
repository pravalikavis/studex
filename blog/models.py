from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

from django.utils import timezone
import os

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    add_image_url = models.TextField()
    product_type=models.CharField(max_length=100,default='stationary')
    product_age=models.IntegerField(default=0)
    product_price=models.IntegerField(default=0)
    phone_no=models.IntegerField(validators=[MinValueValidator(7777777777),
                                              MaxValueValidator(9999999999)], default=9999999999)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                              MaxValueValidator(5)], default=0)

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
