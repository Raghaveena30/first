from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>Hi Jampandu How Are U</h1></marquee>')
def jigelrani(request):
    return HttpResponse('<h1><marquee>Hi Jigelrani How Are U</h1></marquee>')