from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def item_list(request):
    items = Item.objects.all()
    return render(request, 'encyclopedia/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'encyclopedia/item_detail.html', {'item': item})

def item_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    items = Item.objects.all()
    if query:
        items = items.filter(name__icontains=query)
    if category_id:
        items = items.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'encyclopedia/item_list.html', {'items': items, 'query': query, 'categories': categories})
