from django.urls import path
from . import views

app_name = 'fooditems'
urlpatterns = [
    path("", views.index, name="index"),
    path("item/", views.items, name="item"),
    path('<int:item_id>/', views.detail, name='detail'),
]
