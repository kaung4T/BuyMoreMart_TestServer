from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product
from app_controller.Order.models import Cart

class Food:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        if Category.objects.filter(name='Foods').exists():
            foods_id = Category.objects.get(name='Foods')
            foods = Product.objects.filter(category=foods_id.id).order_by('-id')
        else:
            foods = None

        p = Paginator(foods, 12)
        page = request.GET.get("page")

        if foods is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items,
            "cart_noti": cart_len
        }
        return render(request, 'foods/foods.html',
                        context)


    def food_type(self, request, name):
        product = Product.objects.filter(product_type=name)

        
        p = Paginator(product, 2)
        
        page = request.GET.get("page")
        items = p.get_page(page)

        context = {
            "items": items,
            "name": name
        }
        return render(request, 'foods/foods.html',
                        context)



    def food_price(self, request, price_chose):

         
        product = Product.objects.all().order_by("-price")
        product2 = Product.objects.all()

        # if price_chose == "min":
        #     product.order_by("price")

        p = Paginator(product, 2)
        
        page = request.GET.get("page")
        items = p.get_page(page)

        context = {
            "items": items,
            "name": price_chose,

        }
        return render(request, 'foods/foods.html',
                        context)
