from django.contrib import admin

# Register your models here.
from .models import Details, Grocerries, Meals

admin.site.register(Grocerries)
admin.site.register(Meals)
admin.site.register(Details)