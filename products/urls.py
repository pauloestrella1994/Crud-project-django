from django.urls import path
from .views import list_products
from .views import add_products
from .views import update_products
from .views import delete_products

urlpatterns = [
    path('list_products/', list_products, name="list_products"),
    path('add_products/', add_products, name="add_products"),
    path('update/<int:id>/', update_products, name="update_products"),
    path('delete/<int:id>/', delete_products, name="delete_products"),

]