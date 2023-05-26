from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart

class New_arrivals:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        new_arrivals = Product().all_new_items()

        p = Paginator(new_arrivals, 12)
        page = request.GET.get("page")

        if new_arrivals is not None:
            items = p.get_page(page)
        else:
            items = None

        
        # Category group
        if items:
            item_type = new_arrivals
        else:
            item_type = None

        context = {
            "items": items,
            "new_arrivals": new_arrivals,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/new_arrivals.html',
                        context)
    

    def new_type(self, request, name):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        new_arrivals = Product().all_new_items()

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
            item_type = new_arrivals
        else:
            item_type = None

        context = {
            "items": items,
            "new_arrivals": new_arrivals,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/new_arrivals.html',
                        context)


    def new_brand(self, request, brand):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        new_arrivals = Product().all_new_items()

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
            item_type = new_arrivals
        else:
            item_type = None

        context = {
            "items": items,
            "new_arrivals": new_arrivals,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/new_arrivals.html',
                        context)
    