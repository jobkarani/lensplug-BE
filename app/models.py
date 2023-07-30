from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class VehicleLights(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Accessories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Bulbs(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Grilles(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class BumperAndParts(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name