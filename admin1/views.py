from django.shortcuts import render

# Create your views here.
def masterpage(request):
    return render(request,'admin1/master.html')

def dashpage(request):
    return render(request,'admin1/dashboard.html')

def addcategorypage(request):
    return render(request,'admin1/category.html')

def addproductpage(request):
    return render(request,'admin1/product.html')

def orderpage(request):
    return render(request,'admin1/orderdetails.html')

def reviewpage(request):
    return render(request,'admin1/review.html')
