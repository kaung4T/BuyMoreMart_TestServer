from django.shortcuts import render, redirect
from app_controller.Application.models import User, Product_type
from app_controller.Order.models import Cart, Order
from app_controller.Website_Interface.models import Info, Header_ImageGroup

class Order_end:
    def success(self, request, order_id):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

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

            if user_order:
                if user != user_order.user:
                    return redirect(f'/order_fail/{order_id}')
        else:
            return redirect(f'/order_fail/{order_id}')


        context = {
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "cart_noti": cart_len,
            "user_order": user_order,
            "user": user
        }

        return render(request, 'order/order_success.html',
                    context)


    def fail(self, request, order_id):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        
        user_order = None


        if User.objects.filter(id=request.user.id).exists():
            user = User.objects.get(id=request.user.id)
        else:
            user = None
        

        context = {
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "cart_noti": cart_len,
            "user_order": user_order,
            "user": user
        }
        
        return render(request, 'order/order_fail.html',
                    context)
        