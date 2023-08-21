from django.forms.models import BaseModelForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.


# def index(request):
#     item_list = item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'fooditems/index.html', context)

class IndexClassView(ListView):
    model = item
    template_name = 'fooditems/index.html'
    context_object_name = 'item_list'


# def detail(request, item_id):
#     current_item = item.objects.get(pk=item_id)
#     context = {
#         'item': current_item,
#     }
#     return render(request, 'fooditems/detail.html', context)

class FoodDetailView(DetailView):
    model = item
    template_name = "fooditems/detail.html"


# def add_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('fooditems:index')
#     return render(request, 'fooditems/item-form.html', {'form': form})

class CreateItem(CreateView):
    model = item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'fooditems/item-form.html'

    @login_required
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
