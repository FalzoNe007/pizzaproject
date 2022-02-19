from django.db import models
from django.core.validators import RegexValidator


class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        upload_to='pizzeriaImages', blank=True, default='pizzeriaImages/pizzalogo.png')
    email = models.EmailField(max_length=245, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.pizzeria_name + ", " + self.city


class Image(models.Model):
    pizzeria = models.ForeignKey(
        Pizzeria, on_delete=models.CASCADE, blank=True, null=True, related_name='pizzeria_images')
    image = models.ImageField(upload_to='photos')
    image_title = models.CharField(max_length=120, blank=True)
    uploded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-uploded_at']
    
