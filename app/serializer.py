from rest_framework import serializers
from .models import *

class WeddingCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description', 'is_available']

class BabyShowerCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyShowerCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class BridalShowerCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridalShowerCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class ChristmasCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class EasterCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasterCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class FathersDayCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FathersDayCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class MothersDayCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MothersDayCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']


class GraduationCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduationCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']


class ValentinesCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValentinesCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']


class RuracioCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuracioCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class EngagementCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class CoporateCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoporateCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class AnniversaryCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnniversaryCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class BaptismalCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaptismalCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class ChristeningCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristeningCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']

class BirthdayCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthdayCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available']       

class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name')
    category_slug = serializers.CharField(source='blog_category.slug')
    category_id = serializers.IntegerField(source='blog_category.id')
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text','tex2','text3','category_name','category_slug', 'category_id']

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'blogs']