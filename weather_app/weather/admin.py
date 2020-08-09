from django.contrib import admin
from .models import City
from django.db import models

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        ("name", {'fields' : ["name"]}),
        ("Count", {'fields' : ["count"]})
    ]

admin.site.register(City)
