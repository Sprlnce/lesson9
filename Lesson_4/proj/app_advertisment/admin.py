from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'auction', 'price']
    list_filter = ['author', 'title']
    actions = ['delete_description', 'make_auction_as_true']
    
    
    @admin.action(description="Удалить описание выбранных объектов")
    def delete_description(self, request, queryset):
        queryset.update(text='')
        
    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
