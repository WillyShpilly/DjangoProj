from django.contrib import admin, messages
from .models import Category, Goods

# Register your models here.

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "is_available", "category", "brief_info")
    list_display_links = ("name", )
    ordering = ("price",)
    list_editable = ("is_available", "price", "stock",)
    list_per_page = 6
    actions = ("set_available", "set_uavailable")
    search_fields= ("name", )
    readonly_fields = ("slug",)
    list_filter = ("category__name", "is_available", )

    @admin.display(description="Цена общая позиции", ordering='price')
    def brief_info(self, goods: Goods):
        return f"Общая цена: {goods.stock * goods.price} USD"
    
    @admin.action(description="Отметить как вналичии")
    def set_available(self, request, queryset):
        count = queryset.update(is_available=Goods.Status.AVAILABLE)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Отметить как нет в наличии")
    def set_uavailable(self, request, queryset):
        count = queryset.update(is_available=Goods.Status.UAVAILABLE)
        self.message_user(request, f"{count} записей недоступны!", messages.WARNING)    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


# admin.site.register(Category)
# admin.site.register(Goods, GoodsAdmin)