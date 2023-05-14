from django.shortcuts import render


class Cart:
    def home(self, request):
        return render(request, 'order/cart.html')

        