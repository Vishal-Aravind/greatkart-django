from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={ 'slug': ('category_name',)}   # used to automatically fill slug field when category field is filled
    list_display = ('category_name', 'slug')             # used to show these headers in the front page like table

admin.site.register(Category, CategoryAdmin)