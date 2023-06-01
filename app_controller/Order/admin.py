from django.contrib import admin
from app_controller.Order.models import Cart, Order


# Register your models here.
'For Cart'
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 
                    'product',
                    'amount',
                    'total_price']

    def get_ordering(self, request):
        return [('user')]  # sort case insensitive


'For Order'
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id',
                    'user', 
                    # 'all_products',
                    'each_product',
                    'total_items',
                    'grand_total_price',
                    'delivery_fee',
                    'status', 
                    # 'is_member',
                    'time']




admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
