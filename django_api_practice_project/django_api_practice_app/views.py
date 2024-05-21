
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# run server: python manage.py runserver

# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # def update(self, request, pk=None):
        #should i be grabbing stock first? Or really should I be grabbing the customer order, and then be grabbing the vehicle type and 
        #quantity from that and then identifying the correct stock type and then subtracting the order quantity.

        #grab the order from the request data?
        #the following I commented out
        # order = CustomerOrder.objects.get(pk=pk)
        # customer_order_serializer = CustomerOrderSerializer(data = request.data)
        # customer_order_serializer.is_valid(raise_exception=True)
        # customer_order_serializer.save()
        # print('ORDER BABY!', order)

        #grab the vehicle type from that specific order
        #the following I commented out
        # vehicle_type = order.objects.get(vehicle=CustomerOrder.vehicles)
        # print('VEHICLE TYPE BABY!', vehicle_type)

        #grab the quantity from that specific order
        #the following I commented out
        # quantity = order.objects.get(quantity=CustomerOrder.order_quantity)
        # print('VEHICLE ORDER QUANTITY BABY!', quantity)

        
        # this chunk worked yesterday to pull the correct stock when we were specifically trying to update the stock page, but I want
        # to use the above data to update the stock, not just to read when someone is updating stock directly

        #the following i commented out
        # stock = Stock.objects.get(pk=pk)
        # stock_serializer = StockSerializer(data = request.data)
        # stock_serializer.is_valid(raise_exception=True)
        # stock_serializer.save()
        # print('STOCK BABY!  ', stock)



        # vehicle_stock = Vehicle.objects.get(id = stock.stock.id)
        # order_that_i_grabbed = CustomerOrder.objects.get(id=id).first()
        # print(order_that_i_grabbed)
        # print(vehicle_stock)
        # vehicle_type_from_order = order_that_i_grabbed.vehicles
        # stock = vehicle_type_from_order.stock - order_that_i_grabbed.order_quantity 

        #the following I commented out
        # return Response()
        

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleInOrderViewSet(viewsets.ModelViewSet):
    queryset = VehicleInOrder.objects.all()
    serializer_class = VehicleInOrderSerializer

    #this is just changing the read, how it is showing up 
    def retrieve(self, request, pk=None):
        order = VehicleInOrder.objects.get(pk=pk)
        vehicleInOrder_serializer = VehicleInOrderSerializer(order)
        data = vehicleInOrder_serializer.data
        # data['vehicle_type'] is the same thing as saying data.vehicle_type
        data['vehicle_type'] = get_order_details(order)
        # data['quantity_of_specific_ordered_vehicle'] = get_order_details(order)
        return Response(data)
        # data['vehicle_type'] = 437

    #this is gonna be list
    def list(self, request):
        queryset = self.get_queryset()
        serializer = VehicleInOrderSerializer(queryset, many=True)
        # vehicleInOrder_serializer = VehicleInOrderSerializer(order)
        data = serializer.data
        # data['vehicle_type'] is the same thing as saying data.vehicle_type
        for d in data:
            d.vehicle_type = get_order_details(d)
        
        # data['quantity_of_specific_ordered_vehicle'] = get_order_details(order)
        return Response(data)
        
        
def get_order_details(obj):
    if (obj.vehicle_type == '1'):
        return 'unicycle'
    elif (obj.vehicle_type == '2'):
        return 'bicycle'
    elif (obj.vehicle_type == '3'):
        return 'tricycle'
    else:
        return 'not a bike'
        


class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

    # def create(self, request):
    #     vehicle_order_data = VehicleInOrder.objects.all()
    #     copy_of_data_being_sent = request.data.copy()
    #     copy_of_data_being_sent[''] = f'{copy_of_data_being_sent} {vehicle_order_data}'

    #     serializer = CustomerOrderSerializer(data=copy_of_data_being_sent)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)


