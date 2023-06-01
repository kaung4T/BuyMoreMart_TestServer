from django.db import models

# Create your models here.

class One_IndexImageGroup(models.Model):
    image1 = models.ImageField(upload_to='website_interface')
    image2 = models.ImageField(upload_to='website_interface')
    image3 = models.ImageField(upload_to='website_interface')

class Two_IndexImageGroup(models.Model):
    image1 = models.ImageField(upload_to='website_interface')
    image2 = models.ImageField(upload_to='website_interface')
    image3 = models.ImageField(upload_to='website_interface')

class Three_IndexImageGroup(models.Model):
    image1 = models.ImageField(upload_to='website_interface')
    image2 = models.ImageField(upload_to='website_interface')
    image3 = models.ImageField(upload_to='website_interface')

class Four_IndexImageGroup(models.Model):
    image1 = models.ImageField(upload_to='website_interface')
    image2 = models.ImageField(upload_to='website_interface')
    image3 = models.ImageField(upload_to='website_interface')


