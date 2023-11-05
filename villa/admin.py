from django.contrib import admin
from .models import *

class AllVillaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'views')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(AllVilla, AllVillaAdmin)
admin.site.register(Category, CategoryAdmin)

