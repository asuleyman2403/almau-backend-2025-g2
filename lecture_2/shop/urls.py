from django.urls import path
from .views import get_products_list, get_product

urlpatterns = [
    path('', get_products_list),
    path('<int:pk>/', get_product)
]

