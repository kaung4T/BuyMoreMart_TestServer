from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Application.models import User, Cart, Category, Product
from django.http import Http404


class Index:
    def home(self, request, id):
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
            "user_cart_item": user_cart_item
        }
        return render(request, 'others/product.html',
                    context)
