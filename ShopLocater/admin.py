from django.contrib import admin
from .models import Task

class ShopDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "name",  "pictures")

admin.site.register(Task,  ShopDetailAdmin)
