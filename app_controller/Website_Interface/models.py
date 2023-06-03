from django.db import models

# Create your models here.


class Info(models.Model):
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.URLField(null=True, blank=True)
    buy_more_mart_info = models.TextField(max_length=255, null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    messenger_link = models.URLField(null=True, blank=True)


class Header_ImageGroup(models.Model):
    name = models.CharField(max_length=255, default='Edit', null=True, blank=True)

    one_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    one_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)

    two_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    two_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    
    three_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    three_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)

    four_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    four_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)

    five_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    five_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)


class Index_ImageGroup(models.Model):
    name = models.CharField(max_length=255, default='Edit', null=True, blank=True)

    one_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    one_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    one_image3 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)

    two_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    two_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    two_image3 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    
    three_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    three_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    three_image3 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)

    four_image1 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    four_image2 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)
    four_image3 = models.ImageField(upload_to='website_interface', null=True, blank=True, default=None)


