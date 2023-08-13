from django.shortcuts import render
from django.http import HttpResponse
from .models import item
from django.template import loader

# Create your views here.


def index(request):
    item_list = item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'fooditems/index.html', context)


def items(request):
    return HttpResponse("<h1>This is an item</h1>")


def detail(request, item_id):
    current_item = item.objects.get(pk=item_id)
    context = {
        'item': current_item,
    }
    return render(request, 'fooditems/detail.html', context)
