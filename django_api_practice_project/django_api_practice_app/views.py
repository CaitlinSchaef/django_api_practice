
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def update(self, request, pk=None):
        stock = Stock.objects.get(pk=pk)
        stock_serializer = StockSerializer(data = request.data)
        stock_serializer.is_valid(raise_exception=True)
        stock_serializer.save()

        # vehicle_stock = Vehicle.objects.get(id=stock.vehicle_stock.id)
        # if (int(request.data['stock'])):



class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

