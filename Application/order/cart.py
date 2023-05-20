from django.shortcuts import render, redirect
from Application.models import User, Cart, Product
from django.http import JsonResponse, HttpResponse

class Cart_class:
    def home(self, request):

        if request.user.is_authenticated:
            items = Cart.objects.filter(user=request.user)
            total_item = Cart().total_item(request.user)
            total_type = len(list(items))
        else:
            items = None
            total_item = 0
            total_type = 0

        context = {
            "items": items,
            "total_item": total_item,
            "total_type": total_type
        }
        return render(request, 'order/cart.html',
                    context)

    
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
                if product.discount:
                    Cart.objects.create(user=user, product=product, total_price=product.discount)
                else:
                    Cart.objects.create(user=user, product=product, total_price=product.price)
                context = {
                "response": "added"
                }
                return JsonResponse(context)
            
            return JsonResponse(context)

        context = {
            "response": ""
            }
        return JsonResponse(context)
    

    def one_product_add_cart(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated == False:
                context = {
                "response": "no_user"
                }
                return JsonResponse(context)

            product_id = request.POST['one_product_id']
            product_new_amount = request.POST['amount']


            product = Product.objects.get(id=product_id)
            user = User.objects.get(id=request.user.id)

            if product.discount:
                new_total_price = int(product_new_amount) * product.discount
            else:
                new_total_price = int(product_new_amount) * product.price


            if product_new_amount:
                if Cart.objects.filter(user=user, product=product).exists():
                    existing_cart = Cart.objects.get(user=user, product=product)

                    if existing_cart.amount == int(product_new_amount):
                        context = {
                        "response": "duplicate"
                        }
                        return JsonResponse(context)
                    else:
                        existing_cart.amount = product_new_amount
                        existing_cart.total_price = new_total_price

                        existing_cart.save()
                        context = {
                        "response": "added"
                        }
                        return JsonResponse(context)


            if Cart.objects.filter(user=user, product=product).exists():
                context = {
                "response": "duplicate"
                }
                return JsonResponse(context)
            else:
                if product.discount:
                    Cart.objects.create(user=user, product=product, total_price=product.discount)
                else:
                    Cart.objects.create(user=user, product=product, total_price=product.price)
                context = {
                "response": "added"
                }
                return JsonResponse(context)
            
            return JsonResponse(context)

        context = {
            "response": ""
            }
        return JsonResponse(context)
