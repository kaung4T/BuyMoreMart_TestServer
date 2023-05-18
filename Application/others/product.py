from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Application.models import User, Category, Product
from django.http import Http404


class Index:
    def home(self, request, id):
        try:
            item = Product.objects.get(id=id)
        except Exception:
            raise Http404

        context = {
            "item": item
        }
        return render(request, 'others/product.html',
                    context)
