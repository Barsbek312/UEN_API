from rest_framework import viewsets
from user.serializers import (UserSerializer, VolonteerSerializer, 
                              OrganizationSerializer,
                              ModeratorSerializer, ApplicationOrganizationSerializer,
                              FavouriteOrganizationSerializer, RegistrationDocumentsSerializer,
                              FavouriteVolonteerSerializer, ApplicationRedactorSerializer,
                              ApplicationVolonteerSerializer, RedactorSerializer)
from user.models import (User, Volonteer, Organization, Moderator, ApplicationOrganization,
                         FavouriteOrganization, RegistrationDocuments, FavouriteVolonteer,
                         ApplicationRedactor, ApplicationVolonteer, Redactor)
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from user.permissions import IsModerator


class RegistrationDocumentsViewSet(viewsets.ModelViewSet):
    queryset = RegistrationDocuments.objects.all()
    serializer_class = RegistrationDocumentsSerializer
    permission_classes = [permissions.AllowAny]


class RedactorViewSet(viewsets.ModelViewSet):
    queryset = Redactor.objects.all()
    serializer_class = RedactorSerializer
    permission_classes = [permissions.AllowAny|IsModerator]


class FavouriteOrganizationViewSet(viewsets.ModelViewSet):
    queryset = FavouriteOrganization.objects.all()
    serializer_class = FavouriteOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavouriteVolonteerViewSet(viewsets.ModelViewSet):
    queryset = FavouriteVolonteer.objects.all()
    serializer_class = FavouriteVolonteerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationVolonteerViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVolonteer.objects.all()
    serializer_class = ApplicationVolonteerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['delete', 'update', 'list']:
            return [IsModerator() or permissions.IsAdminUser()]
        elif self.action in ['list', 'create',]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


class ApplicationRedactorViewSet(viewsets.ModelViewSet):
    queryset = ApplicationRedactor.objects.all()
    serializer_class = ApplicationRedactorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['delete', 'update', 'list']:
            return [IsModerator() or permissions.IsAdminUser()]
        elif self.action in ['list', 'create',]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


class ApplicationOrganizationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationOrganization.objects.all()
    serializer_class = ApplicationOrganizationSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['delete', 'update', 'list']:
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