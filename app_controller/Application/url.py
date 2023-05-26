from django.urls import path
from app_controller.Application import views

from app_controller.Application.foods import foods
from app_controller.Application.accessories import accessories
from app_controller.Application.gb import gb
from app_controller.Application.website import header

from app_controller.Application.others import discount
from app_controller.Application.others import new_arrivals
from app_controller.Application.others import products
from app_controller.Application.others import profile
from app_controller.Application.others import product


urlpatterns = [
    path('', views.Index().home, name='index'),
    path('search', views.Index().search, name='search'),
    path('header_bmm', header.Index().header, name='header_bmm'),


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




    # one page of a product 
    path('product/<str:id>/', product.Index().home, name='product'),

    
    path('foods', foods.Food().home, name='foods'),
    path('foods/food_type/<str:name>/', foods.Food().food_type, name='food_type'),
    path('foods/food_price/<str:price_chose>/', foods.Food().food_price, name='food_price'),
    path('foods/food_brand/<str:brand>/', foods.Food().food_brand, name='food_brand'),



    path('accessories', accessories.Accessories().home, name='accessories'),
    path('accessories/accessories_type/<str:name>/', accessories.Accessories().accessories_type, name='accessories_type'),
    path('accessories/accessories_brand/<str:brand>/', accessories.Accessories().accessories_brand, name='accessories_brand'),



    path('gb', gb.Gb().home, name='gb'),
    path('beauty/beauty_type/<str:name>/', gb.Gb().beauty_type, name='beauty_type'),
    path('beauty/beauty_brand/<str:brand>/', gb.Gb().beauty_brand, name='beauty_brand'),



    path('discount', discount.Discount().home, name='discount'),
    path('discount/discount_type/<str:name>/', discount.Discount().discount_type, name='discount_type'),
    path('discount/discount_brand/<str:brand>/', discount.Discount().discount_brand, name='discount_brand'),



    path('new_arrivals', new_arrivals.New_arrivals().home, name='new_arrivals'),
    path('new/new_type/<str:name>/', new_arrivals.New_arrivals().new_type, name='new_type'),
    path('new/new_brand/<str:brand>/', new_arrivals.New_arrivals().new_brand, name='new_brand'),


    # all products
    path('products', products.Products().home, name='products'),
    path('products/products_type/<str:name>/', products.Products().products_type, name='products_type'),
    path('products/products_brand/<str:brand>/', products.Products().products_brand, name='products_brand'),

]
