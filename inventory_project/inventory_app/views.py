from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item



# CRUD= create, read, update, delete
# Home View

def home_view(request):
    return render(request, 'inventory_app/home.html')

# Create View
def product_create_view(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'inventory_app/product_form.html', {'form': form})


# Read View
def product_list_view(request):
    items= Item.objects.all()
    return render(request, 'inventory_app/product_list.html', {'items': items})



# Update View
def product_update_view(request, item_id):
    item=Item.objects.get(item_id=item_id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'inventory_app/product_form.html', {'form': form})


# Delete View
def product_delete_view(request, item_id):
    item=Item.objects.get(item_id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('product_list')
    return render(request, 'inventory_app/product_confirm_delete.html', {'item': item})




