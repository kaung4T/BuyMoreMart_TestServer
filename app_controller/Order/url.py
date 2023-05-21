from django.urls import path
from app_controller.Application import views

from app_controller.Order.order import cart, order_complete


urlpatterns = [
    # order
    path('cart', cart.Cart_class().home, name='cart'),
    path('add_cart', cart.Cart_class().add_cart, name='add_cart'),
    path('one_product_add_cart', cart.Cart_class().one_product_add_cart, name='one_product_add_cart'),
    path('order_success', order_complete.Order().success, name='order_success'),
    path('order_fail', order_complete.Order().fail, name='order_fail'),
    
    ]
