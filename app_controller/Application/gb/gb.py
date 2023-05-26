from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart

class Gb:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        if Category.objects.filter(id=3).exists():
            beauty_id = Category.objects.get(id=3)
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')
        else:
            beauty = None

        p = Paginator(beauty, 12)
        page = request.GET.get("page")

        if beauty is not None:
            items = p.get_page(page)
        else:
            items = None


        # Category group
        if Category.objects.filter(id=3).exists():
            categrory_id = Category.objects.get(id=3)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None


        context = {
            "items": items,
            "beauty": beauty,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'gb/gb.html',
                        context)
        

    def beauty_type(self, request, name):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        if Category.objects.filter(id=3).exists():
            beauty_id = Category.objects.get(id=3)
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')
        else:
            beauty = None
            

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
        if Category.objects.filter(id=3).exists():
            categrory_id = Category.objects.get(id=3)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None

        context = {
            "items": items,
            "beauty": beauty,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'gb/gb.html',
                        context)


    def beauty_brand(self, request, brand):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        if Category.objects.filter(id=3).exists():
            beauty_id = Category.objects.get(id=3)
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')
        else:
            beauty = None
            

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
        if Category.objects.filter(id=3).exists():
            categrory_id = Category.objects.get(id=3)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None

        context = {
            "items": items,
            "beauty": beauty,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'gb/gb.html',
                        context)
    