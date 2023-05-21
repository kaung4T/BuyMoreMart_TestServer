from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product

class Accessories:
    def home(self, request):
        if Category.objects.filter(name='Accessories').exists():
            accessories_id = Category.objects.get(name='Accessories')
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')
        else:
            accessories = None

        p = Paginator(accessories, 12)
        page = request.GET.get("page")

        if accessories is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items
        }
        return render(request, 'accessories/accessories.html',
                        context)
        