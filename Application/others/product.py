from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Application.models import User, Category, Product



class Index:
    def home(self, request, id):
        item = Product.objects.get(id=id)

        context = {
            "item": item
        }
        return render(request, 'others/product.html',
                    context)
