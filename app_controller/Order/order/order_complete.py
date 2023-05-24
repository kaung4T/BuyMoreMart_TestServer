from django.shortcuts import render, redirect
from app_controller.Application.models import User
from app_controller.Order.models import Cart, Order

class Order_end:
    def success(self, request, order_id):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0


        try:
            if Order.objects.filter(order_id=order_id).exists():
                user_order = Order.objects.get(order_id=order_id)
            else:
                user_order = None
        except:
            user_order = None
            return redirect(f'/order_fail/{order_id}')


        if User.objects.filter(id=request.user.id).exists():
            user = User.objects.get(id=request.user.id)
        else:
            user = None


        context = {
            "cart_noti": cart_len,
            "user_order": user_order,
            "user": user
        }

        return render(request, 'order/order_success.html',
                    context)


    def fail(self, request, order_id):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        
        try:
            if Order.objects.filter(order_id=order_id).exists():
                user_order = Order.objects.get(order_id=order_id)
            else:
                user_order = None
        except:
            user_order = None
        

        context = {
            "cart_noti": cart_len
        }
        
        return render(request, 'order/order_fail.html',
                    context)
        