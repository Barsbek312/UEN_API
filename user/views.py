from rest_framework import viewsets
from user.serializers import (UserSerializer, VolonteerSerializer, SellerSerializer,
                         OrganizationSerializer)
from user.models import User, Volonteer, Seller, Organization
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class VolonteerViewSet(viewsets.ModelViewSet):
    queryset = Volonteer.objects.all()
    serializer_class = VolonteerSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = VolonteerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            try:
                user = User.objects.get(username=user)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if Seller.objects.filter(user=user).exists():
                return Response({'message': 'This user is seller'}, status=status.HTTP_400_BAD_REQUEST)
            
            elif Organization.objects.filter(user=user).exists():
                return Response({'message': 'This user is organization'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Volonteer added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            try:
                user = User.objects.get(username=user)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if Volonteer.objects.filter(user=user).exists():
                return Response({'message': 'This user is volonteer'}, status=status.HTTP_400_BAD_REQUEST)
            
            elif Organization.objects.filter(user=user).exists():
                return Response({'message': 'This user is organization'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Seller added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            try:
                user = User.objects.get(username=user)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if Seller.objects.filter(user=user).exists():
                return Response({'message': 'This user is seller'}, status=status.HTTP_400_BAD_REQUEST)
            
            elif Volonteer.objects.filter(user=user).exists():
                return Response({'message': 'This user is volonteer'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Organization added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)