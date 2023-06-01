from django.contrib import admin
from app_controller.Website_Interface.models import Index_ImageGroup
# Register your models here.



class Index_ImageGroupAdmin(admin.ModelAdmin):
    list_display = ['one_image1',
                    'one_image2',
                    'one_image3',
                    'two_image1',
                    'two_image2',
                    'two_image3',
                    'three_image1',
                    'three_image2',
                    'three_image3',
                    'four_image1',
                    'four_image2',
                    'four_image3']


admin.site.register(Index_ImageGroup, Index_ImageGroupAdmin)

