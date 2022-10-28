from operator import mod
from django.db import models
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Brand Name: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category Name: {self.name}"


class Product(models.Model):
    name = models.CharField("Product Name", max_length=100, default="no-name", help_text="This")
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product Name: {self.name}"
    
class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product in stocks: {self.product.name}"
    

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return f"City: {self.name}"
    


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"Customer : {self.name}"

    
class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"Customer: {self.customer.name} | Total Amount: {self.total_amount}"