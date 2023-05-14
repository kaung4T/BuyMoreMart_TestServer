from django.shortcuts import render


class Accessories:
    def home(self, request):
        return render(request, 'accessories/accessories.html')
        