
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def update(self, request, pk=None):
        #should i be grabbing stock first? Or really should I be grabbing the customer order, and then be grabbing the vehicle type and 
        #quantity from that and then identifying the correct stock type and then subtracting the order quantity.

        #grab the order from the request data?
        order = CustomerOrder.objects.get(pk=pk)
        customer_order_serializer = CustomerOrderSerializer(data = request.data)
        customer_order_serializer.is_valid(raise_exception=True)
        customer_order_serializer.save()
        print('ORDER BABY!', order)

        #grab the vehicle type from that specific order
        vehicle_type = order.objects.get(vehicle=CustomerOrder.vehicles)
        print('VEHICLE TYPE BABY!', vehicle_type)

        #grab the quantity from that specific order
        quantity = order.objects.get(quantity=CustomerOrder.order_quantity)
        print('VEHICLE ORDER QUANTITY BABY!', quantity)

        
        # this chunk worked yesterday to pull the correct stock when we were specifically trying to update the stock page, but I want
        # to use the above data to update the stock, not just to read when someone is updating stock directly
        stock = Stock.objects.get(pk=pk)
        stock_serializer = StockSerializer(data = request.data)
        stock_serializer.is_valid(raise_exception=True)
        stock_serializer.save()
        print('STOCK BABY!  ', stock)



        # vehicle_stock = Vehicle.objects.get(id = stock.stock.id)
        # order_that_i_grabbed = CustomerOrder.objects.get(id=id).first()
        # print(order_that_i_grabbed)
        # print(vehicle_stock)
        # vehicle_type_from_order = order_that_i_grabbed.vehicles
        # stock = vehicle_type_from_order.stock - order_that_i_grabbed.order_quantity 
        return Response()
        

#I want to update the stock of the vehicle based upon the customer order's order_quantity


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

