
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import upbit_price
def index(request):
    print(get_price('USDT-BTC'))
    return render(request, 'test.html')