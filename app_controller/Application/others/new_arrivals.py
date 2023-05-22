from django.shortcuts import render
from django.core.paginator import Paginator
from app_controller.Application.models import Category, Product
from app_controller.Order.models import Cart

class New_arrivals:
    def home(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        new_arrivals = Product().all_new_items()

        p = Paginator(new_arrivals, 12)
        page = request.GET.get("page")

        if new_arrivals is not None:
            items = p.get_page(page)
        else:
            items = None

        context = {
            "items": items,
            "cart_noti": cart_len
        }
        return render(request, 'others/new_arrivals.html',
                        context)
        