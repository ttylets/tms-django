from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('categories/', views.categories_view, name='categories'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('products/', views.products_view, name='products'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
