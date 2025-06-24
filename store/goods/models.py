from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=1)


class Goods(models.Model):
    class Status(models.IntegerChoices):
        UNAVAILABLE = 0, "Not available"  
        AVAILABLE = 1, "Available"  


    name = models.CharField(max_length=100, verbose_name="Валына")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(blank=True, verbose_name="На складе")
    image = models.ImageField(upload_to='firearms/', blank=True, verbose_name="Изображение")
    slug = models.SlugField(unique=True, blank=True, db_index=True, verbose_name="slug")
    is_available = models.IntegerField(choices=Status, default=Status.AVAILABLE, verbose_name="Наличие")  

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


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
