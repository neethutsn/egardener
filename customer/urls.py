from django.urls import path
from . import views


urlpatterns=[

    path('homemaster/',views.masterpage,name="master"),
    path('home/',views.homepage,name="home"),
    path('dashboard/',views.dashpage,name="dashmaster"),
    path('register/',views.registerpage,name="register"),
    path('signin/',views.loginpage,name="signin"),
    path('cart/',views.cartpage,name="cart"),
    path('profile/',views.profilepage,name="profile"),
    path('bonsai/',views.bonsaipage,name="bonsai"),
    path('flowering/',views.floweringpage,name="flowering"),
    path('gift/',views.giftpage,name="gift"),
    path('indoor/',views.indoorpage,name="indoor"),
    path('outdoor/',views.outdoorpage,name="outdoor"),
    path('shopmaster/',views.shopmasterpage,name="shopmaster"),



]