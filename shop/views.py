from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("We are on about")

def track(request):
    return HttpResponse("We are on tracker")
    
def contact(request):
    return HttpResponse("We are on contact")

def productView(request):
    return HttpResponse("We are on product view")

def checkout(request):
    return HttpResponse("We are on checkout")

def pay(request):
    return HttpResponse("We are on payment page")

def cart(request):
    return HttpResponse("We are on cart page")