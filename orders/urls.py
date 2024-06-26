from django.urls import path
from .views import order_list,checkout,add_to_cart
from .api import OrderApi,OrderDetailApi,Apply_Copoun,Create_update_delete_Cart,CreatOrderApi

urlpatterns = [
    path('',order_list),
    path('checkout',checkout),
    path('add_to_cart',add_to_cart),

    # api

    path('<str:username>/orderlistapi',OrderApi.as_view()),
    path('<str:username>/orderapi/<int:pk>',OrderDetailApi.as_view()),
    path('<str:username>/apply_copoun',Apply_Copoun.as_view()),
    path('<str:username>/createorder',CreatOrderApi.as_view()),
    path('<str:username>/update_delete cart',Create_update_delete_Cart.as_view()),


]
