from django.db import models


class Destination(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city, self.country


class Product(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    invoice = models.PositiveIntegerField(unique=True)
    price = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, unique=True)
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class Contractor(models.Model):
    name = models.CharField(max_length=30, unique=True)
    certificate_number = models.CharField(max_length=12, unique=True)
    city = models.OneToOneField(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
