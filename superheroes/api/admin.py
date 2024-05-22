from django.contrib import admin
from .models import Hero

# Register your models here.

class SuperHeroesAdmin(admin.ModelAdmin):
    list_display = ('alias', 'powers', 'rate_power')
    
    search_fields = ('alias', 'name')

admin.site.register(Hero, SuperHeroesAdmin)