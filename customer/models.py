from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_name = models.TextField(max_length=20)
    cust_email = models.TextField(max_length=50)
    cust_mobile = models.TextField(max_length=50)
    cust_address = models.TextField(max_length=100)
    cust_pwd = models.TextField(max_length=20)
    
class Category(models.Model):
    cat_name = models.TextField(max_length=50)
    cat_plantname = models.TextField(max_length=50)
    
    