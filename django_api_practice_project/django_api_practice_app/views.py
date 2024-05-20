
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
# python views.py  


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def update(self, request, pk=None):
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

