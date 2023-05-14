from django.shortcuts import render


class Order:
    def success(self, request):
        return render(request, 'order/order_success.html')

    def fail(self, request):
        return render(request, 'order/order_fail.html')
        