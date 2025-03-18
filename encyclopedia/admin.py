from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Отображаемые колонки в списке
    search_fields = ('name', 'category')  # Поля для поиска
    list_filter = ('category',)  # Фильтр по категориям
    ordering = ('name',)  # Сортировка по алфавиту
