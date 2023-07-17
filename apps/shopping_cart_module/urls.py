from django.urls import path
from apps.shopping_cart_module import views
app_name = "order"


urlpatterns = [

    path('order/add-to-order', views.add_to_order,name="addd-to-order"),
    path('order/user-cart', views.User_Cart.as_view(),name="user-cart"),
    path('order/delete-user-cart/',views.delete_order,name='delete-user-cart'),
    path('order/change-user-cart/',views.change_order_cart,name='change-user-cart')

]
