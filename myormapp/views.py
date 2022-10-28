from ast import Or
from calendar import month
from datetime import date
from multiprocessing import context
from django.shortcuts import render
from .models import City, Country, Orders
from django.db.models import Sum
# Create your views here.


# def home(request):
#     context = {}
#     cities = City.objects.filter(name__in=["London","Lahore"])
#     print(cities)

#     context = {"cities": cities}
#     return render(request, "home.html", context)

def home(request):
    context = {}

    city = Orders.objects.values('customer__id', 'customer__name', 'customer__email',
                                 'customer__phone').annotate(Sum('total_amount')).order_by('order_date')
    print(city)
    # city = Orders.objects.values('country__name').annotate(sum('total_amount'))
    print("Here")
    for i in city:
        print(i, i)

    context = {"cities": city}
    return render(request, "home.html", context)
