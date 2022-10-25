from django.shortcuts import render
from .models import City
# Create your views here.


def home(request):
    context = {}
    cities = City.objects.filter(name__in=["London","Lahore"])
    print(cities)

    context = {"cities": cities}
    return render(request, "home.html", context)
