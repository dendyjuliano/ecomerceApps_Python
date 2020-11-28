from django.db import models

# Create your models here.

class Category (models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cover_product',null=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Product (models.Model) :
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    description = models.TextField()
    qty = models.IntegerField()
    size = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Shipping (models.Model) :
    name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    size = models.CharField(max_length=50)
    on_packaging = models.IntegerField()
    on_delivery = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    pay_limit = models.DateTimeField()

    def __str__(self):
        return self.name

class Transaction (models.Model) :
    shipping = models.ForeignKey(Shipping,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    qty = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.product
