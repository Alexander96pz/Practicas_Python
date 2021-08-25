from django.urls.conf import path

from .views import product_view_delete, product_view_detail,product_view_create,product_view_list
from django.urls import path
# app_name = 'product'
urlpatterns = [
    path('<int:id>',product_view_detail,name='product-view-detail'),
    path('create',product_view_create,name='product-view-create'),
    path('',product_view_list,name='product-view-list'),
    path('<int:id>/delete',product_view_delete,name='product-view-delete')
]