from django.shortcuts import render
from django.core.paginator import Paginator
from Application.models import Product

class Food:
    def home(self, request):

        if Product.objects.filter(category=1).exists:
            product = Product.objects.filter(category=1)
        else:
            product = None
        
        p = Paginator(product, 2)
        
        page = request.GET.get("page")
        items = p.get_page(page)

        context = {
            "items": items
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
