from django.db import models

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


