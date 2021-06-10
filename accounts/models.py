from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=64, unique=True, blank=False)
    phone = models.CharField(max_length=17, unique=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
	
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=120, blank=False)
    def __str__(self):
        return self.name

class Product(models.Model):
	CATEGORY = (
		('Indoor', 'Indoor'),
		('Out Door', 'Out Door'),
		) 
	name = models.CharField(max_length=200, blank=False)
	price = models.FloatField(default=0, blank=False)
	category = models.CharField(max_length=200, choices=CATEGORY, blank=False)
	description = models.CharField(max_length=200, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
		)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
