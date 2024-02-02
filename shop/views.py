from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from shop.serializers import ProductSerializer, OrderSerializer, AddressSerializer
from .models import Product, Order, Address
from rest_framework.response import Response
from rest_framework import status


class ProductAPIListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderAPIListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # def get(self, request, *args, **kwargs):
    #     queryset = Order.objects.all()
    #     serializer = OrderSerializer(queryset, many=True)
    #     print(request.query_params)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self,request,*args,**kwargs):
    #     queryset = Order.objects.all()
    #     serializer = OrderSerializer(queryset, many=True)
    #     print(request.data)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class OrderAPIRetriveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

class AddressAPIListCreateView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # def post(self,request,*args,**kwargs):
    #     queryset = Address.objects.all()
    #     serialized = AddressSerializer(queryset, many=True)
    #     # print(request.headers)
    #     return Response(serialized.data, status=status.HTTP_200_OK)

def order_api(request):
    # your order api code here
    ...
