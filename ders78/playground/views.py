from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,Collection,OrderItem


def say_hello(request):
    product = Product.objects.all()[0]

    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).first()

    # --------------

    # to check the existance of an object
    # this will return a boolean value
    # exists = Product.objects.filter(pk=1).exists()
    # return HttpResponse(exists)

    # --------------

    # lets say we want all the products that are 20$
    # queryset = Product.objects.filter(unit_price=20)

    # --------------
    # gt → greater than (>)
    # gte → greater than or equal (>=)
    # lt → less than (<)
    # lte → less than or equal (<=)
    
    # what if we want products that cost more than 20$
    # queryset = Product.objects.filter(unit_price__gt=20)

    # --------------

    range(20,30)
    queryset = Product.objects.filter(unit_price__range=(20,30)).order_by('unit_price')
    


    return render(request, 'hello.html', {
        'name': 'ebg',
        'products': list(queryset)
    })
