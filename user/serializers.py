from rest_framework import serializers
from user.models import User, Volonteer, Organization, Moderator, Application
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
        fields = ['url', 'id', 'user', 'uen_coins', 'user_name']
        
    def get_user_name(self, obj):
        return obj.user.username
      

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = ['url', 'id', 'city', 'address', 
                  'postal_code', 'phonenumber', 'email', 
                  'user', 'user_name', 'posts']
            
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
    
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'organization']