from django.shortcuts import render
from Application.models import Product, Cart

class Cart:
    def home(self, request):
        return render(request, 'order/cart.html')

    
    def add_cart(self, request, product_id):
        product = Product.objects.get(id=product_id)
        
        Cart.objects.create()

        return