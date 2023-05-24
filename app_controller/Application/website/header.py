from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import Http404
from app_controller.Application.models import User, Category, Product
from app_controller.Application.verification import send_otp, send_email
from app_controller.Application.check_phone import check_phone_num
from app_controller.Order.models import Cart

# Create your views here.


'Index Page Start'
class Index:
    def header(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0


        context = {
            'cart_noti': cart_len,
        }
        return render(request, "header.html",
                    context)