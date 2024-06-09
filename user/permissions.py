from rest_framework.permissions import BasePermission
from user.models import Volonteer, User, Organization, Moderator

class IsVolonteer(BasePermission):
    
    def has_permission(self, request, view):
        return ((Volonteer.objects.filter(user=request.user).exists() and bool(request.user and request.user.is_authenticated))
                or request.user.is_staff)
    

class IsOrganization(BasePermission):
    
    def has_permission(self, request, view):
        return ((Organization.objects.filter(user=request.user).exists() and bool(request.user and request.user.is_authenticated))
                or request.user.is_staff)
        

class IsModerator(BasePermission):
    
    def has_permission(self, request, view):
        return ((Moderator.objects.filter(user=request.user.id).exists() and bool(request.user and request.user.is_authenticated))
                or request.user.is_staff)