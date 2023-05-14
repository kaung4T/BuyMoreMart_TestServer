from django.urls import path
from Application import views

from Application.foods import foods
from Application.accessories import accessories
from Application.gb import gb

from Application.others import discount
from Application.others import new_arrivals
from Application.others import products
from Application.others import profile
from Application.order import cart, order_complete


urlpatterns = [
    path('', views.Index().home, name='index'),
    path('search', views.Index().search, name='search'),


    path('registration', views.Account().registration, name='registration'),
    path('login', views.Account().login, name='login'),
    path('logout', views.Account().logout, name='logout'),
    path('profile', profile.Profile().home, name='profile'),
    path('security', profile.Profile().security, name='security'),
    path('profile_verification/<str:new_password>/', profile.Profile().profile_verification, name='profile_verification'),

    # account_and_profile_verification 
    path('account_verification/<str:pk>/', views.Account().account_verification, name='account_verification'),
    path('account_resend_otp/<str:pk>/', views.Account().account_resend_otp, name='account_resend_otp'),
    # path('account_verification', profile.Account().account_verification, name='account_verification'),




    # order
    path('cart', cart.Cart().home, name='cart'),
    path('order_success', order_complete.Order().success, name='order_success'),
    path('order_fail', order_complete.Order().fail, name='order_fail'),


    # one page of a product 
    path('product/<str:id>/', views.Index().product, name='product'),

    
    path('foods', foods.Food().home, name='foods'),
    path('foods/food_type/<str:name>/', foods.Food().food_type, name='food_type'),
    path('foods/food_price/<str:price_chose>/', foods.Food().food_price, name='food_price'),



    path('accessories', accessories.Accessories().home, name='accessories'),
    path('gb', gb.Gb().home, name='gb'),

    path('discount', discount.Discount().home, name='discount'),
    path('new_arrivals', new_arrivals.New_arrivals().home, name='new_arrivals'),

    # all products
    path('products', products.Products().home, name='products'),

]
