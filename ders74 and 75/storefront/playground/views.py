from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("Merhabalar")

def render_template(request):
    return render(request,"home.html",{"name":"ebg"})