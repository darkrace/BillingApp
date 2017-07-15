# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.
class Item(models.Model):
	Name = models.CharField(max_length=200)
	Product = models.CharField(max_length=200)
	Price = models.IntegerField()
	Quantity = models.IntegerField()
	Order = models.CharField(max_length=200)
	Date = models.DateField(("Date"), default = date.today)
