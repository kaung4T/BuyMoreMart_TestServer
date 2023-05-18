from django.shortcuts import render, redirect
from Application.models import User, Cart, Product
from django.http import JsonResponse, HttpResponse

class Cart_class:
    def home(self, request):
        return render(request, 'order/cart.html')

    
    def add_cart(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated == False:
                context = {
                "response": "no_user"
                }
                return JsonResponse(context)

            product_id = request.POST['product_id']
            product = Product.objects.get(id=product_id)
            user = User.objects.get(id=request.user.id)


            if Cart.objects.filter(user=user, product=product).exists():
                context = {
                "response": "duplicate"
                }
                return JsonResponse(context)
            else:
                Cart.objects.create(user=user, product=product)
                context = {
                "response": "added"
                }
                return JsonResponse(context)
            
            return JsonResponse(context)

        context = {
            "response": ""
            }
        return JsonResponse(context)