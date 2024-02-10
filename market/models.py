from django.db import models
from user.models import User, Seller

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return self.name
    

class FavouriteProfuct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favourite_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourited_by_users')