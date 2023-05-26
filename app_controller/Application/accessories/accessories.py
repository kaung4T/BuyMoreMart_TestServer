from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart

class Accessories:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        if Category.objects.filter(id=2).exists():
            accessories_id = Category.objects.get(id=2)
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')
        else:
            accessories = None

        p = Paginator(accessories, 12)
        page = request.GET.get("page")

        if accessories is not None:
            items = p.get_page(page)
        else:
            items = None

        # Category group
        if Category.objects.filter(id=2).exists():
            categrory_id = Category.objects.get(id=2)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None

        context = {
            "items": items,
            "accessories": accessories,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'accessories/accessories.html',
                        context)
        
    
    def accessories_type(self, request, name):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        if Category.objects.filter(id=2).exists():
            accessories_id = Category.objects.get(id=2)
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')
        else:
            accessories = None
            

        # data
        if Product_type.objects.filter(name=name).exists():
            pt = Product_type.objects.get(name=name)
            product = Product.objects.filter(product_type=pt.id)
        else:
            product = None
        
        p = Paginator(product, 12)
        
        page = request.GET.get("page")

        if product is not None:
            items = p.get_page(page)
        else:
            items = None


        # Category group
        if Category.objects.filter(id=2).exists():
            categrory_id = Category.objects.get(id=2)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None

        context = {
            "items": items,
            "accessories": accessories,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'accessories/accessories.html',
                        context)


    def accessories_brand(self, request, brand):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        if Category.objects.filter(id=2).exists():
            accessories_id = Category.objects.get(id=2)
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')
        else:
            accessories = None
            

        # data
        if Product.objects.filter(brand=brand).exists():
            product = Product.objects.filter(brand=brand)
        else:
            product = None
        
        p = Paginator(product, 12)
        
        page = request.GET.get("page")

        if product is not None:
            items = p.get_page(page)
        else:
            items = None


        # Category group
        if Category.objects.filter(id=2).exists():
            categrory_id = Category.objects.get(id=2)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None

        context = {
            "items": items,
            "accessories": accessories,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'accessories/accessories.html',
                        context)