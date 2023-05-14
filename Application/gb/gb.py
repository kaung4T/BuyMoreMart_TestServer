from django.shortcuts import render


class Gb:
    def home(self, request):
        return render(request, 'gb/gb.html')
        