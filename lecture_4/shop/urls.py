from django.urls import path
from .views import get_products_list, get_product, delete_product_view, get_index_page

urlpatterns = [
    path('', get_index_page, name='index_page'),
    path('products/', get_products_list, name='products_list_page'),
    path('products/<int:pk>/', get_product, name='product_details_page'),
    path('products/<int:pk>/delete/', delete_product_view, name='delete_product')
]

