from django.urls import path
from .views import get_products_list, get_product, delete_product_view

urlpatterns = [
    path('', get_products_list),
    path('<int:pk>/', get_product),
    path('<int:pk>/delete/', delete_product_view)
]

