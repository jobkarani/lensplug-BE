from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class VehicleLightsCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'vehiclelightscategory'
        verbose_name_plural = 'vehiclelightscategories'

    def get_url(self):
        return reverse('vehiclelights_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class VehicleLights(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(VehicleLightsCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class AccessoriesCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'accessorycategory'
        verbose_name_plural = 'accessorycategories'

    def get_url(self):
        return reverse('accessories_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    
class Accessories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(AccessoriesCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class BulbsCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'bulbscategory'
        verbose_name_plural = 'bulbscategories'

    def get_url(self):
        return reverse('bulbs_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    
class Bulbs(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(BulbsCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class GrillesCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'grillescategory'
        verbose_name_plural = 'grillescategories'

    def get_url(self):
        return reverse('grilles_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Grilles(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(GrillesCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class BumperAndPartsCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'bumperandpartscategory'
        verbose_name_plural = 'bumperandpartscategories'

    def get_url(self):
        return reverse('bumperandparts_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    
class BumperAndParts(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(BumperAndPartsCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name