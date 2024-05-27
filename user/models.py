from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.username
    

class Volonteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volonteer')
    passport_photo = models.ImageField(upload_to='volonteers_passport/')
    volonteer_type = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='volonteers/')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    instagram = models.CharField(max_length=400, null=True, default=None)
    facebook = models.CharField(max_length=400, null=True, default=None)
    youtube = models.CharField(max_length=400, null=True, default=None)
    telegram = models.CharField(max_length=400, null=True, default=None)


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    city = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=400, null=True, default=None)
    facebook = models.CharField(max_length=400, null=True, default=None)
    youtube = models.CharField(max_length=400, null=True, default=None)
    telegram = models.CharField(max_length=400, null=True, default=None)
    image1 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image2 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image3 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image4 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image5 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image6 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image7 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image8 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    image9 = models.ImageField(blank=True, null=True, upload_to='organizations/')
    
    def __str__(self) -> str:
        return self.user.username
    

class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='moderator')
    

class Redactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='redactor')
    passport_photo = models.ImageField(upload_to='redactors_passport/')
    application_statement = models.TextField()
    city = models.CharField(max_length=500)
    country = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='redactors/')
    description = models.TextField()
    instagram = models.CharField(max_length=400, null=True, default=None)
    facebook = models.CharField(max_length=400, null=True, default=None)
    youtube = models.CharField(max_length=400, null=True, default=None)
    telegram = models.CharField(max_length=400, null=True, default=None)


class ApplicationRedactor(models.Model):
    passport_photo = models.ImageField(upload_to='redactors_passport/')
    application_statement = models.TextField()
    city = models.CharField(max_length=500)
    country = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='redactors/')
    description = models.TextField()
    instagram = models.CharField(max_length=400, null=True, default=None)
    facebook = models.CharField(max_length=400, null=True, default=None)
    youtube = models.CharField(max_length=400, null=True, default=None)
    telegram = models.CharField(max_length=400, null=True, default=None)
    accepted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        password = None

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

        if password:
            subject = 'Your Account Information'
            message = render_to_string('email_template.txt', {
                'username': self.name,
                'password': password,
            })

            from_email = 'your@example.com'
            to_email = [self.email]
            send_mail(subject, message, from_email, to_email)

        super().save(*args, **kwargs)

class ApplicationOrganization(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=100)
    type_organization = models.CharField(max_length=100)
    email = models.EmailField()
    INN = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    website_link = models.CharField(max_length=200)
    representative_organizations = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    goals_description = models.TextField()
    logo = models.ImageField(upload_to='organization_logo/')
    instagram = models.CharField(max_length=400, null=True, default=None)
    facebook = models.CharField(max_length=400, null=True, default=None)
    youtube = models.CharField(max_length=400, null=True, default=None)
    telegram = models.CharField(max_length=400, null=True, default=None)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        password = None

        if self.accepted:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

            
            user = User.objects.create_user(
                username=self.name,
                email=self.email,
                phone_number = self.phone_number,
                password=password
            )
            
                
            Organization.objects.create(
                user=user,
                city=self.city,
                address=self.address,
                postal_code=self.postal_code,
            )

        if password:
            subject = 'Your Account Information'
            message = render_to_string('email_template.txt', {
                'username': self.name,
                'password': password,
            })

            from_email = 'your@example.com'
            to_email = [self.email]
            send_mail(subject, message, from_email, to_email)

        super().save(*args, **kwargs)
        

class RegistrationDocuments(models.Model):
    application = models.ForeignKey(ApplicationOrganization, on_delete=models.CASCADE, related_name='app_registration_documents')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, default=None, related_name='org_registration_documents')
    file = models.FileField(upload_to='registration_documents/')


class FavouriteOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_user')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='favourite_org')
    

class FavouriteVolonteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_vol_user')
    volonteer = models.ForeignKey(Volonteer, on_delete=models.CASCADE, related_name='favourite_vol')