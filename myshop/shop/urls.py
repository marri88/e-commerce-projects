from django.urls import path
from . import views

urlpatterns = [
    path('(?P<id>\d+)/', views.product_detail, name='product_detail'),
    path('', views.product_list, name='product_list'),
    path('(?P<category_slug>[-\w]+)/', views.product_list, name='product_list_by_category'),
]
