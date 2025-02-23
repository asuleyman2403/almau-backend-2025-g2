from django.urls import path
from .views import get_products_list, get_product, delete_product_view, get_index_page, edit_product, get_categories_list, edit_category, delete_category, get_category_products

urlpatterns = [
    path('', get_index_page, name='index_page'),

    path('categories/', get_categories_list, name='categories_list_page'), # GET List, POST
    path('categories/<int:pk>/edit', edit_category, name='edit_category'),
    path('categories/<int:pk>/delete', delete_category, name='delete_category'),
    path('categories/<int:pk>/products', get_category_products, name='category_product_list'),


    path('products/', get_products_list, name='products_list_page'),
    path('products/<int:pk>/', get_product, name='product_details_page'),
    path('products/<int:pk>/edit/', edit_product, name='edit_product'),
    path('products/<int:pk>/delete/', delete_product_view, name='delete_product')
]

