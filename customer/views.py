from django.shortcuts import render

# Create your views here.
def masterpage(request):
    return render(request,'customer/homemaster.html')

def homepage(request):
    return render(request,'customer/home.html')

def dashpage(request):
    return render(request,'customer/dashboard.html')

def registerpage(request):
    return render(request,'customer/register.html')

def loginpage(request):
    return render(request,'customer/signin.html')

def cartpage(request):
    return render(request,'customer/cart.html')

def profilepage(request):
    return render(request,'customer/profile.html')

def bonsaipage(request):
    return render(request,'customer/bonsai.html')

def floweringpage(request):
    return render(request,'customer/flowering.html')

def giftpage(request):
    return render(request,'customer/gift.html')

def indoorpage(request):
    return render(request,'customer/indoor.html')

def outdoorpage(request):
    return render(request,'customer/outdoor.html')

def shopmasterpage(request):
    return render(request,'customer/shopmaster.html')

