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
            "category_key": "Type",
            "category_value": name,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'accessories/accessories.html',
                        context)

    

    def accessories_price(self, request, price_chose):
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

        # for min value 
        if price_chose == "min_price":
            if Category.objects.filter(id=2).exists():
                categrory_id = Category.objects.get(id=2)
                product = Product.objects.filter(category=categrory_id.id).order_by("price")
            else:
                product = None
            
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
            if Category.objects.filter(id=2).exists():
                categrory_id = Category.objects.get(id=2)
                product2 = Product.objects.filter(category=categrory_id.id).order_by("-price")
            else:
                product2 = None
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
        if Category.objects.filter(id=2).exists():
            categrory_id = Category.objects.get(id=2)
            item_type = Product_type.objects.filter(category=categrory_id.id).order_by('-id')
        else:
            item_type = None
        
        if price_chose == "min_price":
            price_info = "min-max"
        elif price_chose == "max_price":
            price_info = "max-min"
        else:
            price_info = None

        context = {
            "items": items,
            "accessories": accessories,
            "category_key": "Price",
            "category_value": price_info,
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
            "category_key": "Brand",
            "category_value": brand,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'accessories/accessories.html',
                        context)
