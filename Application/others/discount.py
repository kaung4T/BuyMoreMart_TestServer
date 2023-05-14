from django.shortcuts import render


class Discount:
    def home(self, request):
        return render(request, 'others/discount.html')
        