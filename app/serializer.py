from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'id', 'user', 'firstname', 'lastname', 'profile_photo',
            'email', 'phone', 'date_joined'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'image1', 'image2', 'image3', 'description',
            'new_price', 'old_price', 'is_available', 'category'
        )

class CartIdentifierSerializer(serializers.Serializer):
    cart_id = serializers.CharField(max_length=32)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_id', 'date_added')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'user', 'product', 'cart', 'quantity', 'is_active')