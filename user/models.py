from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_judical = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    

class Volonteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volonteer')
    uen_coins = models.IntegerField(default=0)
    
    def increase_coins(self, value):
        self.uen_coins += value
        self.save()
        
    def decrease_coins(self, value):
        if self.uen_coins > 0:
            self.uen_coins -= value
            self.save()
            

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name