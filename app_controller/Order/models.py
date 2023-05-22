from django.db import models
from app_controller.Application.models import User, Product
import uuid
from django.utils.html import mark_safe
from django.conf import settings
# Create your models here.


'For cart'
class Cart(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    total_price = models.IntegerField()

    def total_item(self, user):
        carts = Cart.objects.filter(user=user)
        total_amount = 0

        for each_cart in carts:
            total_amount += each_cart.amount

        return total_amount

    def all_total_price(self, user):
        carts = Cart.objects.filter(user=user)
        all_price = 0
        
        for each_cart in carts:
            all_price += each_cart.total_price

        return all_price

'For order'
class Order(models.Model):
    choice = [
        ["Pending", "Pending"],
        ["Approved", "Approved"]
    ]

    is_memberChoice = [
        ["True", "True"],
        ["False", "False"],
    ]

    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name="order_products", help_text="အညိုရောင်နောက်ခံမှတ်ထားသောပစ္စည်းများသည် Customer ဝယ်ထားသောပစ္စည်းများ ဖြစ်ပါသည်။")
    each_product = models.TextField(help_text="နံပါတ်များသည် မှာယူထားသော ပစ္စည်း အရေအတွက် ဖြစ်သည်။")
    total_items = models.IntegerField(default=1)
    grand_total_price = models.IntegerField(help_text="ပစ္စည်းအားလုံး နှင့် Delivery fee စုစုပေါင်းကျသင့်ငွေ။")
    delivery_fee = models.IntegerField()
    status = models.CharField(max_length=225, default="Pending", choices=choice)
    # is_member = models.CharField(max_length=225, default="False", choices=is_memberChoice)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def all_products(self):
        return "\n".join([p.title for p in self.product.all()])

