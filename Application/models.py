from django.db import models
from django.contrib.auth.models import AbstractUser, User
import uuid
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.


'For Emergency User Profile'
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='media', null=True, blank=True)



'For User'
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    otp = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)


'For category'
class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


'for product type'
class Product_type(models.Model):
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


'For Product'
class Product(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='products_image')
    image2 = models.ImageField(upload_to='products_image', null=True, blank=True, default=None)
    image3 = models.ImageField(upload_to='products_image', null=True, blank=True, default=None)
    image4 = models.ImageField(upload_to='products_image', null=True, blank=True, default=None)
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=1028, null=True, blank=True)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, help_text="Category 3 မျိုးထည်း မှ ရွေးချယ်ပေးပါ။")
    product_type = models.ForeignKey(Product_type, default=None, on_delete=models.CASCADE, help_text="အမျိုးအစားများ အကန့်အသတ် မရှိထက်ထည့်နိုင်သည်။")
    brand = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    new_arrival = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image != '':
            # return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.image))
            return mark_safe(f'<img src="{self.image.url}" width="130" height="130" style="object-fit: contain;" />')
    
    def limit_discount_items(self):
        discount_list = []
        all_product = Product.objects.all().order_by('-id')
        for each_product in all_product:
            if each_product.discount:
                discount_list.append(each_product) 

            if len(discount_list) == 6:
                break

        if len(discount_list) == 0:
            discount_list = None
        return discount_list



    def limit_new_items(self):
        new_arrivals_list = []
        all_product = Product.objects.all().order_by('-id')
        for each_product in all_product:
            if each_product.new_arrival == True:
                new_arrivals_list.append(each_product)
            
            if len(new_arrivals_list) == 12:
                break

        if len(new_arrivals_list) == 0:
            new_arrivals_list = None
        return new_arrivals_list



    def all_discount_items(self):
        discount_list = []
        all_product = Product.objects.all().order_by('-id')
        for each_product in all_product:
            if each_product.discount:
                discount_list.append(each_product) 
        
        if len(discount_list) == 0:
            discount_list = None
        return discount_list



    def all_new_items(self):
        new_arrivals_list = []
        all_product = Product.objects.all().order_by('-id')
        for each_product in all_product:
            if each_product.new_arrival == True:
                new_arrivals_list.append(each_product)

        if len(new_arrivals_list) == 0:
            new_arrivals_list = None
        return new_arrivals_list


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
    amount = models.IntegerField(default=1)
    status = models.CharField(max_length=225, default="Pending", choices=choice)
    is_member = models.CharField(max_length=225, default="False", choices=is_memberChoice)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def all_products(self):
        return "\n".join([p.title for p in self.product.all()])

