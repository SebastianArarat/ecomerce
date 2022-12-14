from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
            name = models.CharField(max_length=200)
            price = models.FloatField()
            digital = models.BooleanField(default=False,null=True, blank=True)
            image = models.ImageField(null=True, blank=True)

            def __str__(self):
                return self.name

            @property
            def imageURL(self):
                try:
                    url = self.image.url
                except:
                    url = ''
                return url

 