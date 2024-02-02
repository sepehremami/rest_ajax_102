from rest_framework import serializers
from .models import Product, Order, Address


class ProductSerializer(serializers.ModelSerializer):
    test = serializers.SerializerMethodField()
    creation_date = serializers.SerializerMethodField()
    modified_date = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'test']

    def get_test(self, obj):
        return 'hello world'

    def get_creation_date(self, obj):
        return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")

    def get_modified_date(self, obj):
        return obj.modified_date.strftime("%Y-%m-%d %H:%M:%S")


class OrderSerializer(serializers.ModelSerializer):
    creation_date = serializers.SerializerMethodField()
    modified_date = serializers.SerializerMethodField()
    order_date = serializers.SerializerMethodField()
    # product = ProductSerializer()

    # ordered_products = serializers.SerializerMethodField()
    class Meta:
        model = Order
        depth = 2
        fields = '__all__'

    def get_creation_date(self, obj):
        return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")

    def get_modified_date(self, obj):
        return obj.modified_date.strftime("%Y-%m-%d %H:%M:%S")

    def get_order_date(self, obj):
        return obj.order_date.strftime("%Y-%m-%d %H:%M:%S")

    # def get_ordered_products(self, obj):
    #

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'