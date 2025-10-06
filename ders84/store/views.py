from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# django (httpResponse) --API--> Response
# django (httpRequest) --API--> Request


@api_view()
def product_list(request):
    return Response('ok')

