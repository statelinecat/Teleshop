from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers')

    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Каталог цветов'

    def __str__(self):
        return self.name
