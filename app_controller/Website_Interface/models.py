from django.db import models

# Create your models here.

class Index_ImageGroup(models.Model):
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


