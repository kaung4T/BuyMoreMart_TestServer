from django.urls import path
from app_controller.Application import views

from app_controller.Order.order import cart, order_complete, order


urlpatterns = [
    # order
    path('cart', cart.Cart_class().home, name='cart'),
    path('cancel_cart/<str:cart_item_id>/', cart.Cart_class().cancel_cart, name='cancel_cart'),
    path('add_cart', cart.Cart_class().add_cart, name='add_cart'),
    path('one_product_add_cart', cart.Cart_class().one_product_add_cart, name='one_product_add_cart'),
    path('order_success', order_complete.Order().success, name='order_success'),
    path('order_fail', order_complete.Order().fail, name='order_fail'),
    
    path('order', order.Order_class().check_out, name='order'),

    ]
