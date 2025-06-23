from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})
    

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=1)


class Goods(models.Model):
    class Status(models.IntegerChoices):
        UNAVAILABLE = 0, "Not available"  
        AVAILABLE = 1, "Available"  


    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(blank=True)
    image = models.ImageField(upload_to='firearms/', blank=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    is_available = models.IntegerField(choices=Status, default=Status.AVAILABLE)  

    objects = models.Manager()
    available = AvailableManager()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('firearm', kwargs={'a_good_slug': self.slug})


    
