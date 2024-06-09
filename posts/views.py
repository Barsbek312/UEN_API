from rest_framework import permissions
from rest_framework import viewsets
from posts.models import (Post, PostLike, Comment, Favourite, 
                          CommentAnswer, CommentLike, CommentAnswerLike)

from posts.serializers import (CommentAnswerLikeSerializer, PostLikeSerializer, 
                               FavouriteSerializer, CommentLikeSerializer, 
                               CommentAnswerSerializer, CommentSerializer, 
                               PostSerializer) 

from posts.permissions import IsVolonteer, IsOrganization, IsModerator, IsRedactor
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.action in ['list']:
    #         return [permissions.AllowAny()]
    #     elif self.action in ['delete', 'update', 'create']:
    #         return [IsModerator or permissions.IsAdminUser or IsRedactor or IsOrganization]
    #     return super().get_permissions()

    

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        print(self)
        instance = serializer.save()
        instance.post.increase()
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.post.decrease()
        self.perform_destroy(instance)
        return Response({ "message" : "Deleted successfully" }, status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        if self.action in ['list']:
            return [permissions.AllowAny()]
        elif self.action in ['delete', 'update', 'create', 'list']:
            return [IsModerator() or permissions.IsAdminUser() or IsRedactor() or IsOrganization()]
        return super().get_permissions()

    

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated|IsModerator]
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated|IsModerator]
    

class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated|IsModerator]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.post.increase()
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.post.decrease()
        self.perform_destroy(instance)
        return Response({ "message" : "Deleted successfully" }, status=status.HTTP_204_NO_CONTENT)


class CommentAnswerViewSet(viewsets.ModelViewSet):
    queryset = CommentAnswer.objects.all()
    serializer_class = CommentAnswerSerializer
    permission_classes = [permissions.IsAuthenticated|IsModerator]
    

class CommentAnswerLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentAnswerLike.objects.all()
    serializer_class = CommentAnswerLikeSerializer
    permission_classes = [permissions.IsAuthenticated|IsModerator]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.post.increase()
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.post.decrease()
        self.perform_destroy(instance)
        return Response({ "message" : "Deleted successfully" }, status=status.HTTP_204_NO_CONTENT)