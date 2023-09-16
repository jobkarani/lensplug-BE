from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile_photo = ImageField( manual_crop="")
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()

    def update(self):
        self.save()

    def create_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username

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
    
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image1 = ImageField( manual_crop="")
    image2 = ImageField(blank=True,null=True, manual_crop="")   
    image3 = ImageField(blank=True,null=True, manual_crop="")
    description = models.TextField(max_length=1000)
    new_price = models.FloatField()
    old_price = models.FloatField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_id = models.CharField(max_length=250, blank=False, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.new_price * self.quantity

    def __unicode__(self):
        return self.product