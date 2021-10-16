from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product_set automatically django accept reverse relationships
class Collection(models.Model):
    title = models.CharField(max_length=255)
    peatured_product = models.ForeignKey('Product' , on_delete=SET_NULL , null=True , related_name='+')
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8 , decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Collection , on_delete=PROTECT)    # one To Many Relationships 
    promotions = models.ManyToManyField(Promotion)   

class Customer(models.Model):
    MEMBERCHIP_BRONZE = 'B'
    MEMBERCHIP_SILVER = 'S'
    MEMBERCHIP_GOLD = 'G'
    MEMBERCHIPS_CHOICES = [
        (MEMBERCHIP_BRONZE , 'Bronze'),
        (MEMBERCHIP_SILVER , 'Silver'),
        (MEMBERCHIP_GOLD , 'Gold'),
    ]
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255 , unique=True)
    phone = models.CharField(max_length=13 , unique=True)
    birth_date = models.DateField(null=True)
    memberships = models.CharField(max_length=2 , choices=MEMBERCHIPS_CHOICES)
class Order(models.Model):
    placed_at = models.DateTimeField(auto_now=True)
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLATE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING , 'Pending'),
        (PAYMENT_STATUS_COMPLATE , 'Complate'),
        (PAYMENT_STATUS_FAILED , 'Failed')
    ]
    payment_status = models.CharField(max_length=1 , choices=PAYMENT_STATUS , default=PAYMENT_STATUS_PENDING)
    #One To Many Relationships between Order and Customer
    customer = models.ForeignKey(Customer , on_delete=PROTECT)



class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer , on_delete=CASCADE)
   # customer = models.OneToOneField(Customer , on_delete=CASCADE , ForeignKey=True)  #One to One Relationships
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=PROTECT)
    product = models.ForeignKey(Product , on_delete=PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=8 , decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    order = models.ForeignKey(OrderItem , on_delete=CASCADE)
    cart = models.ForeignKey(Cart , on_delete=CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag , on_delete=models.CASCADE)

    #Type(Product , Video , Article)
    content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()