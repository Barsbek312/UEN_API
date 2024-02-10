from rest_framework import serializers
from user.models import User, Volonteer, Seller, Organization
from djoser.serializers import UserCreateSerializer


class VolonteerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Volonteer
        fields = ['url', 'id', 'user', 'uen_coins', 'user_name']
        
    def get_user_name(self, obj):
        return obj.user.username
        

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Seller
        fields = ['url', 'id', 'user', 'user_name']
          
    def get_user_name(self, obj):
        return obj.user.username
      

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Organization
        fields = ['url', 'id', 'name', 'user', 'user_name']
            
    def get_user_name(self, obj):
        return obj.user.username


class UserRegistrationSerializer(UserCreateSerializer):
    volonteer = VolonteerSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'seller', 'organization']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    volonteer = VolonteerSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'password','is_active',
                  'volonteer', 'seller', 'organization']