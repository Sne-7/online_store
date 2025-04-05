from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


from django.views import View
from django.http import JsonResponse

class ProductListView(View):
    def get(self, request):
        data = {
            "products": [
                {"id": 1, "name": "T-shirt", "price": 499},
                {"id": 2, "name": "Jeans", "price": 899},
            ]
        }
        return JsonResponse(data)

