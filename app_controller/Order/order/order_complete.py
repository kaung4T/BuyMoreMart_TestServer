from django.shortcuts import render
from app_controller.Order.models import Cart

class Order:
    def success(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        context = {
            "cart_noti": cart_len
        }

        return render(request, 'order/order_success.html',
                    context)

    def fail(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        context = {
            "cart_noti": cart_len
        }
        
        return render(request, 'order/order_fail.html',
                    context)
        