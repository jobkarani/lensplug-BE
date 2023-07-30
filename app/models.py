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

class BabyShowerCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class BridalShowerCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class ChristmasCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class EasterCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class FathersDayCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class MothersDayCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class GraduationCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class ValentinesCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class RuracioCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class EngagementCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class CoporateCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class AnniversaryCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class BaptismalCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class BirthdayCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class ChristeningCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class WeddingCakes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=4000)
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'blogcategory'
        verbose_name_plural = 'blogcategories'

    def get_url(self):
        return reverse('blogs_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Blogs(models.Model):
    image = ImageField( manual_crop="")
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, blank=False, null=True)
    tex2 = models.TextField(max_length=1000, blank=True, null=True)
    text3 = models.TextField(max_length=1000, blank=True, null=True)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading