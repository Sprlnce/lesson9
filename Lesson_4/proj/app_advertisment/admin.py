from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'price', 'auction', 'created_date', 'update_date', 'get_image'] # 
    list_filter = ['author', 'title']
    actions = ['delete_description', 'make_auction_as_true', 'make_auction_as_false']
    readonly_fields = ["get_image"]
    # fieldsets = ( # при добавлении записей указываем кастомизацию
    #     (   # блок 1
    #         'Общее', # название блока
    #         {
    #             "fields":('title', 'text', 'author'),
    #         }
    #     ),
    #     (   # блок 2
    #         'Финансы', # название блока
    #         {
    #             "fields":('price', 'auction'),
    #             "classes":['collapse'] # для скрытия
    #         }
    #     ) 
    # )
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
    
    get_image.short_description = "Изображение"
    
    
    @admin.action(description="Удалить описание выбранных объектов")
    def delete_description(self, request, queryset):
        queryset.update(text='')
        
    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset:QuerySet):
        print(queryset, type(queryset))
        queryset.update(auction=True)

    @admin.action(description="Отключить возможность торга")
    def make_auction_as_false(self, request, queryset:QuerySet):
        print(queryset, type(queryset))
        queryset.update(auction=False)

    
    

admin.site.register(Advertisement, AdvertisementAdmin)
