# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate , get_user_model , login , logout )

def index(request ):
    a = Item.objects.all()
    return render(request ,  'Billing/index.html' ,{"a":a} )

def Item_detail(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Product = request.POST.get('Product')
        Quantity = request.POST.get('Quantity')
        if Quantity == "Toffy" :
            Price = (int(Quantity)*150)+(int(Quantity)*12)
        elif Quantity == "Jelly" :
            Price = (int(Quantity)*200)+(int(Quantity)*12)
        elif Quantity == "Lollipop" :
            Price = (int(Quantity)*250)+(int(Quantity)*12)
        else :
            Price = (int(Quantity)*350)+(int(Quantity)*12)
        Order = 'pending'
        Date = request.POST.get('Date')
        Item_Obj =Item(Name = Name, Product = Product , Price = Price , Quantity = Quantity , Order = Order , Date = Date)
        
        
        Item_Obj.save()
    return HttpResponseRedirect('/index#services')

def Price_Detail(request):
    if request.method == 'POST':
        Product = request.POST.get('Product')
        Quantity = request.POST.get('Quantity')
        if Quantity == "Toffy" :
            Price = (int(Quantity)*150)+(int(Quantity)*12)
        elif Quantity == "Jelly" :
            Price = (int(Quantity)*200)+(int(Quantity)*12)
        elif Quantity == "Lollipop" :
            Price = (int(Quantity)*250)+(int(Quantity)*12)
        else :
            Price = (int(Quantity)*350)+(int(Quantity)*12)
    return HttpResponseRedirect('/index#gallery', Price )
