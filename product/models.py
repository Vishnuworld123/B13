from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # One-to-Many relationship: One User -> Many Products
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='products')

    def __str__(self):
        return f"{self.name} -- {self.price}"


# when? what? purpose?  --> 
# python manage.py migrate