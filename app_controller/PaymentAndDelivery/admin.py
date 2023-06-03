from django.contrib import admin
from app_controller.PaymentAndDelivery.models import Payment_type, Delivery_fee
# Register your models here.


'For Payment'
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'iamge']


'For Order'
class DeliveryFeeAdmin(admin.ModelAdmin):
    list_display = ['city',
                    'delivery_fee',
                    'free']

    # def has_add_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False




admin.site.register(Payment_type, PaymentTypeAdmin)
admin.site.register(Delivery_fee, DeliveryFeeAdmin)
