from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import TestSquare

class TestSquareDetail(admin.ModelAdmin):
    list_display=('Number','SquareNumber')
admin.site.register(TestSquare,TestSquareDetail)
