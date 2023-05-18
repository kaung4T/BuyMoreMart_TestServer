from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Application.models import User, Category, Product
from django.http import Http404


class Index:
    def home(self, request, id):
        try:
            item = Product.objects.get(id=id)
            suggest_items = Product.objects.filter(category=item.category).order_by('-id')[:12]
        except Exception:
            raise Http404

        context = {
            "item": item,
            "suggest_items": suggest_items
        }
        return render(request, 'others/product.html',
                    context)
