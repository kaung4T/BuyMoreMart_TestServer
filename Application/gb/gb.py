from django.shortcuts import render
from django.core.paginator import Paginator
from Application.models import Category, Product

class Gb:
    def home(self, request):
        if Category.objects.filter(name='Beauty').exists():
            beauty_id = Category.objects.get(name='Beauty')
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')
        else:
            beauty = None

        p = Paginator(beauty, 12)
        page = request.GET.get("page")

        if beauty is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items
        }
        return render(request, 'gb/gb.html',
                        context)
        