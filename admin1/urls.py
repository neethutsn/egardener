from django.urls import path
from . import views

urlpatterns=[

    path('master/',views.masterpage,name="adminmaster"),
    path('dashboard/',views.dashpage,name="admindashboard"),
    path('category/',views.addcategorypage,name="admincategory"),
    path('product/',views.addproductpage,name="adminproduct"),
    path('orderdetails/',views.orderpage,name="orderdetails"),
    path('review/',views.reviewpage,name="review"),


]