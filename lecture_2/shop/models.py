from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f'ID {self.id}, name: {self.name}'

