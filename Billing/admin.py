# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display=['Name' ,'Product', 'Price' , 'Quantity' , 'Order' , 'Date']

admin.site.register(Item , ItemAdmin)
