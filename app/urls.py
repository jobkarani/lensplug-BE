from django.urls import path
from app import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    # path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('generate-cart-id/', views.generate_cart_id, name='generate_cart_id'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove-cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove-cart-item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/', views.cart, name='cart'),
]
