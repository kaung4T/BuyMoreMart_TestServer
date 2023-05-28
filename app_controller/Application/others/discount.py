from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart

class Discount:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        discount = Product().all_discount_items()

        p = Paginator(discount, 12)
        page = request.GET.get("page")
        
        if discount is not None:
            items = p.get_page(page)
        else:
            items = None


        # Category group
        if items:
            item_type = discount
        else:
            item_type = None

        context = {
            "items": items,
            "discount": discount,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)
    
    

    def discount_type(self, request, name):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        discount = Product().all_discount_items()

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
        if items:
            item_type = discount
        else:
            item_type = None

        context = {
            "items": items,
            "discount": discount,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)



    def discount_price(self, request, price_chose):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        discount = Product().all_discount_items()

        # for min value 
        if price_chose == "min_price":
            product = Product().min_price_all_discount_items()
            product2 = None
        else:
            product = None
        
        if product:
            p = Paginator(product, 12)
            p_page = request.GET.get("page")
            items = p.get_page(p_page)
        # product is for mini and cant be None
        elif product == None and price_chose == "min_price":
            items = None



        # for max value
        if price_chose == "max_price":
            product2 = Product().max_price_all_discount_items()
            product = None
        else:
            product2 = None

        if product2:
            p2 = Paginator(product2, 12)
            p2_page = request.GET.get("page")
            items = p2.get_page(p2_page)
        # product2 is for max and cant be None
        elif product2 == None and price_chose == "max_price":
            items = None

        # Category group
        if items:
            item_type = discount
        else:
            item_type = None


        context = {
            "items": items,
            "discount": discount,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)



    def discount_brand(self, request, brand):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        discount = Product().all_discount_items()

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
        if items:
            item_type = discount
        else:
            item_type = None

        context = {
            "items": items,
            "discount": discount,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)
    