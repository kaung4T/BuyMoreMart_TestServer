from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product
from app_controller.Order.models import Cart

class Discount:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        discount = Product().all_discount_items()

        p = Paginator(discount, 12)
        page = request.GET.get("page")
        
        if discount is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items,
            "cart_noti": cart_len
        }
        return render(request, 'others/discount.html',
                        context)
        