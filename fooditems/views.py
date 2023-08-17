from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import ItemForm

# Create your views here.


def index(request):
    item_list = item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'fooditems/index.html', context)


def detail(request, item_id):
    current_item = item.objects.get(pk=item_id)
    context = {
        'item': current_item,
    }
    return render(request, 'fooditems/detail.html', context)


@login_required
def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fooditems:index')
    return render(request, 'fooditems/item-form.html', {'form': form})


@login_required
def update_item(request, id):
    current_item = item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=current_item)
    if form.is_valid():
        form.save()
        return redirect('fooditems:index')
    return render(request, 'fooditems/item-form.html', {'form': form, 'item': current_item})


@login_required
def delete_item(request, id):
    current_item = item.objects.get(id=id)
    if request.method == "POST":
        current_item.delete()
        return redirect('fooditems:index')
    return render(request, 'fooditems/item-delete.html', {'item': current_item})
