from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart
from app_controller.Website_Interface.models import Info, Header_ImageGroup

class Discount:
    def home(self, request):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        discount = Product().all_discount_items()

        p = Paginator(discount, 24)
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
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "items": items,
            "discount": discount,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)
    


    def discount_type(self, request, name):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

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
        
        p = Paginator(product, 24)
        
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
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "items": items,
            "discount": discount,
            "category_key": "Type",
            "category_value": name,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)



    def discount_price(self, request, price_chose):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

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
            p = Paginator(product, 24)
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
            p2 = Paginator(product2, 24)
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

        if price_chose == "min_price":
            price_info = "min-max"
        elif price_chose == "max_price":
            price_info = "max-min"
        else:
            price_info = None

        context = {
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "items": items,
            "discount": discount,
            "category_key": "Price",
            "category_value": price_info,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)



    def discount_brand(self, request, brand):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

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
        
        p = Paginator(product, 24)
        
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
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "items": items,
            "discount": discount,
            "category_key": "Brand",
            "category_value": brand,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'others/discount.html',
                        context)
    