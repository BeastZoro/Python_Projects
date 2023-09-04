from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category/<int:cate_id>/', views.products_category, name='products_category'),
    path("hot_item", views.hot_items, name='hot_items'),
]