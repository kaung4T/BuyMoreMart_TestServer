from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product

class Products:
    def home(self, request):
        all_products = Product.objects.all().order_by('-id')

        p = Paginator(all_products, 12)
        page = request.GET.get("page")

        if all_products is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items
        }
        return render(request, 'others/products.html',
                        context)
        