from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name='subcategory'),
    path('search', SearchView.as_view(), name='search'),
    path('signup', signup , name ='signup'),
    path('contact', contact ,name='contact'),
    path('mycart', CartView.as_view() ,name='mycart'),
    path('checkout', Checkout.as_view() ,name='checkout'),
    path('add_to_cart/<slug>', add_to_cart ,name='add_to_cart'),
   
    path('deletecart/<slug>', deletecart ,name='deletecart'),
    path('reducecart/<slug>', reducecart ,name='reducecart'),
]