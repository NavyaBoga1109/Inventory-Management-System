from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('supplier/add/', views.add_supplier, name='add_supplier'),
    path('supplier/<int:id>/edit/', views.edit_supplier, name='edit_supplier'),
    path('supplier/<int:id>/delete/', views.delete_supplier, name='delete_supplier'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('sale_orders/', views.list_sale_orders, name='list_sale_orders'),
    path('sale_order/add/', views.create_sale_order, name='create_sale_order'),
    path('sale_order/<int:id>/edit/', views.edit_sale_order, name='edit_sale_order'),
    path('sale_order/<int:id>/delete/', views.delete_sale_order, name='delete_sale_order'),
    path('sale_order/<int:id>/cancel/', views.cancel_sale_order, name='cancel_sale_order'),
    path('sale_order/<int:id>/complete/', views.complete_sale_order, name='complete_sale_order'),
    path('stock_movements/', views.list_stock_movements, name='list_stock_movements'),
    path('stock_movements/add/', views.add_stock_movement, name='add_stock_movement'),
    path('stock_levels/', views.stock_levels, name='stock_levels'),



]
