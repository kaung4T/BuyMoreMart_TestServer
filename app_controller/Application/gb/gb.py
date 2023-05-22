from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product
from app_controller.Order.models import Cart

class Gb:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

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
            "items": items,
            "cart_noti": cart_len
        }
        return render(request, 'gb/gb.html',
                        context)
        