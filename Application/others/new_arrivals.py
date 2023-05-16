from django.shortcuts import render
from django.core.paginator import Paginator
from Application.models import Category, Product

class New_arrivals:
    def home(self, request):
        new_arrivals = Product().all_new_items()

        p = Paginator(new_arrivals, 12)
        page = request.GET.get("page")

        if new_arrivals is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items
        }
        return render(request, 'others/new_arrivals.html',
                        context)
        