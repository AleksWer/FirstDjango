from django.contrib import admin
from .models import Item
from .models import Color
# Register your models here.

admin.site.register(Item)
admin.site.register(Color)