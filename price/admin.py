from django.contrib import admin
from .models import Price, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
