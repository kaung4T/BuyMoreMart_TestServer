from django.shortcuts import render, redirect
from Application.models import Product, Cart
from django.http import JsonResponse

class Cart:
    def home(self, request):
        return render(request, 'order/cart.html')

    
    def add_cart(self, request):
        if request.method == 'POST':
            if user.is_authenticated == False:
                redirect('login')

            product_id = request.POST['product_id']
            product = Product.objects.get(id=product_id)


            return redirect('index')

        return redirect('index')