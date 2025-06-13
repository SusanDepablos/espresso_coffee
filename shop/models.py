from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "users"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.email})"
    
class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    description = models.TextField(
        verbose_name='Descripción detallada',
        max_length=500,
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='shop/categories/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    
    class Meta:
        db_table = "categories"
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return self.image.url if self.image else static('shop/img/default.jpeg')

# Create your models here.
