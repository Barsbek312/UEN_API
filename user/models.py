from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string

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


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    city = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.user.username
    

class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='moderator')
    

class Application(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    accepted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        password = None  # Define password variable here

        if self.accepted:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

            
            user = User.objects.create_user(
                username=self.name,
                email=self.email,
                password=password
            )
            
                
            Organization.objects.create(
                user=user,
                city=self.city,
                address=self.address,
                postal_code=self.postal_code,
                phonenumber=self.phonenumber,
                email=self.email
            )

        if password:  # Check if password is not None
            subject = 'Your Account Information'
            message = render_to_string('email_template.txt', {
                'username': self.name,
                'password': password,
            })

            from_email = 'your@example.com'  # Replace with your email
            to_email = [self.email]
            send_mail(subject, message, from_email, to_email)

        super().save(*args, **kwargs)