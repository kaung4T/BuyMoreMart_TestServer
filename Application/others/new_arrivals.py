from django.shortcuts import render


class New_arrivals:
    def home(self, request):
        return render(request, 'others/new_arrivals.html')
        