from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('services', views.services),
    path('aboutus', views.aboutus),
    path('contactus', views.contactus),
    path('regpage', views.regpage),
    path('register', views.register),
    path('inquiry', views.inquiry),
    path('login', views.login),
    path('logout', views.logout),
    path('orders', views.orders),
    path("purchase",views.purchase),
    path("checkout", views.checkout),
    path("cart/<int:product_id>", views.cartadd),
    path("delete/<int:item_id>", views.cartdelete),
    
]

