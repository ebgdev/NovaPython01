from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q ,F , Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count,Min, Max,Avg
from django.db.models.functions import Concat
from store.models import Product,OrderItem,Order,Customer, Collection
from tags.models import TaggedItem

def say_hello(request):
   
    with connection.cursor() as cursor:
        cursor.execute('select id, first_name from store_customer limit 5')
        results = cursor.fetchall()


    return render(request,'hello.html',{'products':results})



# get the last 5 orders with their customer and items including product