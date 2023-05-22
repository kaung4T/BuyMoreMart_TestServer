from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from app_controller.Application.models import User, Category, Product
from app_controller.Order.models import Cart
from django.http import Http404


class Index:
    def home(self, request, id):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        try:
            item = Product.objects.get(id=id)
            suggest_items = Product.objects.filter(category=item.category).order_by('-id')[:12]
        except Exception:
            raise Http404

        try:
            user_cart_item = Cart.objects.get(user=request.user, product=item)
        except:
            user_cart_item = None
        

        context = {
            "item": item,
            "suggest_items": suggest_items,
            "user_cart_item": user_cart_item,
            "cart_noti": cart_len
        }
        return render(request, 'others/product.html',
                    context)
