from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from app_controller.Application.models import User, Category, Product, Product_type
from app_controller.Order.models import Cart
from django.http import Http404
from app_controller.Website_Interface.models import Info, Header_ImageGroup

class Index:
    def home(self, request, id):
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
            item = Product.objects.get(id=id)
            suggest_items = Product.objects.filter(category=item.category).order_by('-id')[:12]
        except Exception:
            raise Http404

        try:
            user_cart_item = Cart.objects.get(user=request.user, product=item)
        except:
            user_cart_item = None
        

        context = {
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "item": item,
            "suggest_items": suggest_items,
            "user_cart_item": user_cart_item,
            "cart_noti": cart_len
        }
        return render(request, 'others/product.html',
                    context)
