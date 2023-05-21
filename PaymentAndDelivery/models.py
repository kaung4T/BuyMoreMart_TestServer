from django.db import models
from django.contrib.auth.models import AbstractUser, User
import uuid
from django.utils.html import mark_safe
from django.conf import settings


class Payment_type(models.Model):
    name = models.CharField(max_length=255)
    iamge = models.ImageField(upload_to="payment_image", null=True, blank=True)

    def __str__(self):
        return self.name


class Delivery_fee(models.Model):
    delivery_fee = models.IntegerField()

