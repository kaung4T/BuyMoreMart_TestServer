from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_controller.Application.models import User, Category, Product_type, Product

# Register your models here.


'For Profile'
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'image']
# 
# 
# admin.site.register(Profile, ProfileAdmin)



'For User'
admin.site.register(User)



'For Category'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


'For Product_type'
class Product_typeAdmin(admin.ModelAdmin):
    list_display = ['category',
                    'name']

    def get_ordering(self, request):
        return [('category')]  # sort case insensitive


'For Product'
class ProductAdmin(admin.ModelAdmin):

    list_display = ['category',
                    'title',
                    'product_type',
                    'name',
                    'image_tag', 
                    # 'description',
                    'brand',
                    'price',
                    'discount',
                    'time',
                    'new_arrival']

    def get_ordering(self, request):
        return [('category')]  # sort case insensitive




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product_type, Product_typeAdmin)

admin.site.register(Product, ProductAdmin)
