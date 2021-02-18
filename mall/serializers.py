from rest_framework import serializers
from mall.models import Bid, Product
from django.contrib.auth.models import User


class BidsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Bid
        fields = ['id', 'value', 'date_published', 'placer', 'product']


class ProductsSerializer(serializers.ModelSerializer):
    bids = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'category', 'upc', 'condition', 'brand', 'description', 'starting_price', 'deadline',
                  'bids', 'owner', 'max_bid']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')
