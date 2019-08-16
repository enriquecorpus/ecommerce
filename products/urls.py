from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.index, name='index'),
    path('product/', products.views.product, name='products_product'),
    path('search/', products.views.products_search, name='products_search'),
    path('ajax/action', products.views.product_action, name='product_action')
]
