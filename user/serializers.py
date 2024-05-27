from rest_framework import serializers
from user.models import User, Volonteer, Organization, Moderator, Application, Redactor
from djoser.serializers import UserCreateSerializer
from posts.serializers import PostSerializer


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['url', 'id', 'name', 'city', 'address', 
                  'postal_code', 'phonenumber', 'email',
                  'accepted']

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
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['url', 'pk', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'organization']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    volonteer = VolonteerSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    redactor = RedactorSerializer(read_only=True)
    is_admin = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'organization', 'redactor', 'is_admin']
        
    def get_is_admin(self, obj):
        return obj.user.is_staff