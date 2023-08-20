from django.urls import path
from . import views

app_name = 'fooditems'
urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path('<int:pk>/', views.FoodDetailView.as_view(), name='detail'),
    path('add', views.add_item, name='add_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
