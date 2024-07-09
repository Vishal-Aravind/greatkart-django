from django.urls import path
from . import views

urlpatterns =[
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),                      # below is the explanation of how the add + button, - button and remove works
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),       # first in carts.views we write the logic to remove, add, minus item in cart then in urls.py we mention the add_cart in views with a endpoint like add_cart/<int:product_id>, then this is added in href of the +,-, remove button. When the button is clicked, the corresponding url is called which adds the number of items in cart. The url called is very fast that you can see that the page gets reloaded but the url will not be visible in th search/url bar.
]