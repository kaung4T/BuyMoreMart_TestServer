from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product, Product_type
from app_controller.Order.models import Cart

class Food:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        if Category.objects.filter(id=1).exists():
            foods_id = Category.objects.get(id=1)
            foods = Product.objects.filter(category=foods_id.id).order_by('-id')
        else:
            foods = None

        p = Paginator(foods, 12)
        page = request.GET.get("page")

        if foods is not None:
            items = p.get_page(page)
        else:
            items = None


        # Category group
        if Category.objects.filter(id=1).exists():
            categrory_id = Category.objects.get(id=1)
            item_type = Product_type.objects.filter(category=categrory_id.id)
        else:
            item_type = None


        context = {
            "items": items,
            "foods": foods,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'foods/foods.html',
                        context)


    def food_type(self, request, name):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        # brand group
        if Category.objects.filter(id=1).exists():
            foods_id = Category.objects.get(id=1)
            foods = Product.objects.filter(category=foods_id.id).order_by('-id')
        else:
            foods = None
            
        
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
        if Category.objects.filter(id=1).exists():
            categrory_id = Category.objects.get(id=1)
            item_type = Product_type.objects.filter(category=categrory_id.id)
        else:
            item_type = None

        context = {
            "items": items,
            "foods": foods,
            "name": name,
            "cart_noti": cart_len,
            "item_type": item_type
        }
        return render(request, 'foods/foods.html',
                        context)



    def food_price(self, request, price_chose):

         
        product = Product.objects.all().order_by("-price")
        product2 = Product.objects.all()

        # if price_chose == "min":
        #     product.order_by("price")

        p = Paginator(product, 12)
        
        page = request.GET.get("page")
        items = p.get_page(page)

        context = {
            "items": items,
            "name": price_chose,

        }
        return render(request, 'foods/foods.html',
                        context)
