from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'ID {self.id}, name: {self.name}'

