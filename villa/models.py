from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class AllVilla(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255, blank=True)
    author_phone_number = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0, blank=True)
    area = models.IntegerField(default=0, blank=True)
    rooms = models.IntegerField(default=0, blank=True)
    bathrooms = models.IntegerField(default=0, blank=True)
    parking = models.IntegerField(default=0, blank=True)
    floor = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


