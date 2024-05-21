from django.db import models

# Create your models here.

# python manage.py makemigrations 
# python manage.py migrate

class Stock(models.Model):
    stock = models.SmallIntegerField(default=10, null=True)

    def __str__(self):
        return f'Number In Stock: {self.stock} of {CustomerOrder.vehicles}'

class Vehicle(models.Model):
    type = models.TextField(max_length=50, default='bicycle', null=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=3500, null=True)
    color = models.TextField(max_length=50, default='black', null=True)

    def __str__(self):
        return f'Type: {self.type}, Price: ${self.price}, Color: {self.color}'


class Customer(models.Model):
    name = models.CharField(max_length=75, null=True)

    def __str__(self):
        return f'Customer Name: {self.name}, Customer ID: {self.id}'

class CustomerOrder(models.Model):
    date_month = models.PositiveIntegerField(default=4)
    date_day = models.PositiveIntegerField(default=12)
    date_year = models.PositiveIntegerField(default=2024)
    customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='names')
    # vehicles = models.ManyToManyField(Vehicle, related_name='order') #type, price, color
    paid = models.TextField(null=True, default='not paid')

    def __str__(self):
        vech_string = ""
        for v in self.vehicles.all():
            vech_string += f"{v}"
        return f'ORDER:{self.id} {self.customer_name}, Vehicles In Order: {self.order_quantity}, Order Date:{self.date_month}-{self.date_day}-{self.date_year}, Paid: {self.paid}: \n \t {vech_string} '
    
class VehicleInOrder(models.Model):
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name="vehicle")
    vehicle_type = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, related_name='vehicle_ordered')
    quantity_of_specific_ordered_vehicle = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'Ordered {self.quantity_of_specific_ordered_vehicle} {self.vehicle_type}s'
    
