from rest_framework import viewsets
from user.serializers import (UserSerializer, VolonteerSerializer, 
                              OrganizationSerializer, ApplicationSerializer,
                              ModeratorSerializer)
from user.models import User, Volonteer, Organization, Application, Moderator
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from user.permissions import IsModerator


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['delete', 'update']:
            return [IsModerator() or permissions.IsAdminUser()]
        elif self.action in ['list', 'create',]:
            return [permissions.AllowAny()]
        return super().get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny|IsModerator]


class VolonteerViewSet(viewsets.ModelViewSet):
    queryset = Volonteer.objects.all()
    serializer_class = VolonteerSerializer
    permission_classes = [permissions.AllowAny|IsModerator]
    
    def create(self, request):
        serializer = VolonteerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            try:
                user = User.objects.get(username=user)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                        
            if Organization.objects.filter(user=user).exists():
                return Response({'message': 'This user is organization'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Volonteer added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny|IsModerator]
    
    def create(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            try:
                user = User.objects.get(username=user)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if Volonteer.objects.filter(user=user).exists():
                return Response({'message': 'This user is volonteer'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'message': 'Organization added successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ModeratorViewSet(viewsets.ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAdminUser|IsModerator]