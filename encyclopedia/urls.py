from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    path('', item_list, name='item_list'),  # Страница со списком предметов
    path('<int:item_id>/', item_detail, name='item_detail'),  # Страница отдельного предмета
]