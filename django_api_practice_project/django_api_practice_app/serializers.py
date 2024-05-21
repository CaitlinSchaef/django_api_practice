from rest_framework import serializers
from .models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'stock']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type', 'stock', 'price', 'color']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'date_month', 'date_day', 'date_year', 'customer_name', 'paid', 'vehicle']

class VehicleInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInOrder
        fields = ['id', 'customer_order', 'vehicle_type', 'quantity_of_specific_ordered_vehicle']

