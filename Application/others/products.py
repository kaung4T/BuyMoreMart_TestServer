from django.shortcuts import render


class Products:
    def home(self, request):
        return render(request, 'others/products.html')
        