"""
URL configuration for django_api_practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from django.urls import path, include

from django_api_practice_app.views import *

#now define router:
router = routers.DefaultRouter()

router.register('stocks', StockViewSet)
router.register('vehicles', VehicleViewSet)
router.register('customers', CustomerViewSet)
router.register('customerOrders', CustomerOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
