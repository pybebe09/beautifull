from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    img = models.ImageField(upload_to='product/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=20, unique=True, blank=True, null=True)
    joylash = models.CharField(max_length=20, choices=(('caro', 'Carousel'),('pro', 'Product')))

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=20)
    bio=models.TextField()
    img=models.ImageField(upload_to='about/')


    def __str__(self):
        return self.title

class Client(models.Model):
        name=models.CharField(max_length=20)
        txt=models.TextField()
        img=models.ImageField(upload_to='customers/')

        def __str__(self):
            return self.name

