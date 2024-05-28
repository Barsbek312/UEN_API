from rest_framework import serializers
from user.models import (User, Volonteer, Organization, Moderator, ApplicationOrganization, 
                         Redactor, ApplicationVolonteer, ApplicationRedactor, RegistrationDocuments,
                         FavouriteOrganization, FavouriteVolonteer)
from djoser.serializers import UserCreateSerializer
from posts.serializers import PostSerializer


class ApplicationOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationOrganization
        fields = ['url', 'id', 'name', 'city', 'address', 
                  'postal_code',
                  'type_organization', 'email','accepted',
                  'INN', 'phone_number', 'website_link', 
                  'representative_organizations', 'position',
                  'contact', 'goals_description', 'logo',
                  'instagram', 'facebook', 'youtube', 'telegram']


class FavouriteOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavouriteOrganization
        fields = ['url', 'id', 'user', 'organization']
        

class RegistrationDocumentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegistrationDocuments
        fields = ['url', 'id', 'application', 'organization', 'file']


class FavouriteVolonteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavouriteVolonteer
        fields = ['url', 'id', 'user', 'volonteer']
        
        
class ApplicationRedactorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationRedactor
        fields = ['url', 'id', 'user', 'city', 'accepted',
                  'passport_photo', 'application_statement', 'country',
                  'photo', 'description',
                  'instagram', 'facebook', 'youtube', 'telegram']


class ApplicationVolonteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationVolonteer
        fields = ['url', 'id', 'user', 'city', 'accepted',
                  'passport_photo', 'volonteer_type', 'country',
                  'photo', 'description',
                  'instagram', 'facebook', 'youtube', 'telegram']


class ModeratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moderator
        fields = ['url', 'id', 'user']


class VolonteerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Volonteer
        fields = ['url', 'id', 'user', 'user_name', 'description', 'instagram',
            'facebook', 'youtube', 'telegram']
        
    def get_user_name(self, obj):
        return obj.user.username
      

class RedactorSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Redactor      
        fields = ['url', 'id', 'user', 'user_name', 'description','instagram',
            'facebook', 'youtube', 'telegram']


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = ['url', 'id', 'city', 'address', 
                  'postal_code', 'phonenumber', 'email','instagram',
                  'facebook', 'youtube', 'telegram', 'user', 
                  'user_name', 'posts']
            
    def get_user_name(self, obj):
        return obj.user.username
    
    
class UserRegistrationSerializer(UserCreateSerializer):
    volonteer = VolonteerSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    redactor = RedactorSerializer(read_only=True)
    is_admin = serializers.SerializerMethodField()
    favourite_organizations = FavouriteOrganizationSerializer(many=True, read_only=True)
    favourite_volonteer = FavouriteVolonteerSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'first_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'organization', 'redactor', 'is_admin', 'favourite_organizations', 'favourite_volonteer']
        
    def get_is_admin(self, obj):
        return obj.is_staff  


class UserSerializer(serializers.HyperlinkedModelSerializer):
    volonteer = VolonteerSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    redactor = RedactorSerializer(read_only=True)
    is_admin = serializers.SerializerMethodField()
    favourite_organizations = FavouriteOrganizationSerializer(many=True, read_only=True)
    favourite_volonteer = FavouriteVolonteerSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'first_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'organization', 'redactor', 'is_admin', 'favourite_organizations', 
                  'favourite_volonteer']
        
    def get_is_admin(self, obj):
        return obj.is_staff  