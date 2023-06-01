from django.contrib import admin
from app_controller.Website_Interface.models import One_IndexImageGroup, Two_IndexImageGroup, Three_IndexImageGroup, Four_IndexImageGroup
# Register your models here.



class One_IndexImageGroupAdmin(admin.ModelAdmin):
    list_display = ['image1',
                    'image2',
                    'image3']

class Two_IndexImageGroupAdmin(admin.ModelAdmin):
    list_display = ['image1',
                    'image2',
                    'image3']

class Three_IndexImageGroupAdmin(admin.ModelAdmin):
    list_display = ['image1',
                    'image2',
                    'image3']

class Four_IndexImageGroupAdmin(admin.ModelAdmin):
    list_display = ['image1',
                    'image2',
                    'image3']




admin.site.register(One_IndexImageGroup, One_IndexImageGroupAdmin)
admin.site.register(Two_IndexImageGroup, Two_IndexImageGroupAdmin)
admin.site.register(Three_IndexImageGroup, Three_IndexImageGroupAdmin)
admin.site.register(Four_IndexImageGroup, Four_IndexImageGroupAdmin)
