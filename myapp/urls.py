from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('products/', views.product_list, name='product_list'),
    path('orders/<str:period>/', views.order_list, name='order_list'),
    path('orders/7/', views.recent_orders_7, name='recent_orders_7'),
    path('orders/30/', views.recent_orders_30, name='recent_orders_30'),
    path('orders/365/', views.recent_orders_365, name='recent_orders_365'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
]
