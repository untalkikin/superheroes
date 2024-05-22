from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=150)
    alias = models.CharField(max_length=150)
    powers = models.CharField(max_length=300)
    image = models.URLField(help_text="Picture of the superheroe")
    rate_power = models.IntegerField(help_text="Rate of power of the heroe")
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Heroe'
        verbose_name_plural = ' Heroes'