from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_view(request, name):
    return HttpResponse("Hey, "+name+"!")

def age(request, end,birthyear):
    return HttpResponse(int(end) - int(birthyear))

def order(request,burgers,fries,drinks):
    bur = float(burgers) * 4.50
    fri = float(fries) * 1.5
    dri = float(drinks) * 1
    total = bur + fri + dri 
    return HttpResponse(total)