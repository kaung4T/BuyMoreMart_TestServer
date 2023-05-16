from django.shortcuts import render
from django.core.paginator import Paginator
from Application.models import Category, Product

class Discount:
    def home(self, request):
        discount = Product().all_discount_items()

        p = Paginator(discount, 12)
        page = request.GET.get("page")
        
        if discount is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items
        }
        return render(request, 'others/discount.html',
                        context)
        