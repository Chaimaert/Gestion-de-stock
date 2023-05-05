from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def _str_(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='brands/')

    def _str_(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='products/')
    alert = models.PositiveIntegerField()
    Last_Edate = models.DateField()
    Last_Odate = models.DateField()

    def _str_(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    email = models.EmailField()

    def _str_(self):
        return self.supp_name

class Customer(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=20)
    address = models.TextField()

    def _str_(self):
        return self.user_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    qte = models.IntegerField()

    def _str_(self):
        return f"{self.user.user_name} - {self.customer.user_name}"


class DeliveryMan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Stock(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    update_date = models.DateField()

    def _str_(self):
        return self.type

class Facture(models.Model):
    date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE)

    def _str_(self):
        return self.date
