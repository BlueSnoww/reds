from django.contrib import admin
from .models import Tag, Info



class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)



class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted')



admin.site.register(Tag, TagAdmin)
admin.site.register(Info, InfoAdmin)
