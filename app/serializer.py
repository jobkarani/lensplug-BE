from rest_framework import serializers
from .models import *

class VehicleLightsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = VehicleLights
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'price', 'category', 'is_available','category_name','category_slug', 'category_id']

class VehicleLightsCategorySerializer(serializers.ModelSerializer):
    vehiclelights = VehicleLightsSerializer(many=True, read_only=True)
    class Meta:
        model = VehicleLightsCategory
        fields = ['id', 'name', 'slug', 'vehiclelights']

class AccessoriesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'price', 'category', 'is_available','category_name','category_slug', 'category_id']

class AccessoriesCategorySerializer(serializers.ModelSerializer):
    accessories = AccessoriesSerializer(many=True, read_only=True)
    class Meta:
        model = AccessoriesCategory
        fields = ['id', 'name', 'slug', 'accessories']

class BulbsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Bulbs
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'price', 'category', 'is_available','category_name','category_slug', 'category_id']

class BulbsCategorySerializer(serializers.ModelSerializer):
    bulbs = BulbsSerializer(many=True, read_only=True)
    class Meta:
        model = BulbsCategory
        fields = ['id', 'name', 'slug', 'bulbs']

class GrillesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Grilles
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'price', 'category', 'is_available','category_name','category_slug', 'category_id']

class GrillesCategorySerializer(serializers.ModelSerializer):
    grilles = GrillesSerializer(many=True, read_only=True)
    class Meta:
        model = GrillesCategory
        fields = ['id', 'name', 'slug', 'grilles']
    
class BumperAndPartsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = BumperAndParts
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'price', 'category', 'is_available','category_name','category_slug', 'category_id']

class BumperAndPartsCategorySerializer(serializers.ModelSerializer):
    bumperandparts = BumperAndPartsSerializer(many=True, read_only=True)
    class Meta:
        model = BumperAndPartsCategory
        fields = ['id', 'name', 'slug', 'bumperandparts']