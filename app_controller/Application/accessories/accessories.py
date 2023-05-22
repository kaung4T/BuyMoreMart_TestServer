from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product
from app_controller.Order.models import Cart

class Accessories:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

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
            "items": items,
            "cart_noti": cart_len
        }
        return render(request, 'accessories/accessories.html',
                        context)
        