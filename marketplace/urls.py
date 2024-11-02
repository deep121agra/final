from django.urls import path
from . import views  # same folder kei andar jitne bhi views hai sare kei sare yhaa prr aa jayenge

urlpatterns = [
    path('',views.marketplace , name='marketplace'),
    
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),
    #path

    # add to cart path
    path('add_to_cart/<int:food_id>', views.add_to_cart, name='add_to_cart'),
    path('decrease_cart/<int:food_id>', views.decrease_cart, name='decrease_cart'),
    # DELETE CART ITEM
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),

    #search
    path('search/', views.search ,name='search'),
    
]
