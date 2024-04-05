from rest_framework import serializers
from posts.models import (Post, PostLike, Comment, Favourite, 
                          CommentAnswer, CommentLike, CommentAnswerLike)


class CommentAnswerLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentAnswerLike
        fields = ['url', 'id', 'user', 'comment_answer']


class PostLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostLike
        fields = ['url', 'id', 'user', 'post']
        

class FavouriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favourite
        fields = ['url', 'id', 'user', 'post']
        

class CommentLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['url', 'id', 'user', 'comment']


class CommentAnswerSerializer(serializers.HyperlinkedModelSerializer):
    liked_by_user = serializers.SerializerMethodField()
    comment_answer_likes = CommentAnswerLikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = CommentAnswer
        fields = ['url', 'id', 'text', 'date', 'number_of_likes', 
                  'liked_by_user', 'user', 'comment', 'comment_answer_likes']

    def get_liked_by_user(self, obj):
        user = self.context['request'].user
        try:
            return CommentAnswerLike.objects.filter(user=user).exists()
        except:
            return False


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    liked_by_user = serializers.SerializerMethodField()
    comment_likes = CommentLikeSerializer(many=True, read_only=True)
    comment_answers = CommentAnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Comment
        fields = ['url', 'id', 'text', 'date', 'number_of_likes', 
                  'liked_by_user', 'user', 'post', 'comment_likes',
                  'comment_answers']

    def get_liked_by_user(self, obj):
        user = self.context['request'].user
        try:
            return CommentLike.objects.filter(user=user).exists()
        except:
            return False


class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_likes = PostLikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    liked_by_user = serializers.SerializerMethodField()
    is_favourite = serializers.SerializerMethodField()
    organization_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['url', 'id', 'text', 'date', 'number_of_likes', 
                  'liked_by_user', 'is_favourite', 'organization_name',
                  'organization', 'post_likes', 'comments']

    def get_liked_by_user(self, obj):
        user = self.context['request'].user
        try:
            return PostLike.objects.filter(user=user).exists()
        except:
            return False

    def get_is_favourite(self, obj):
        user = self.context['request'].user
        try:
            return Favourite.objects.filter(user=user).exists()
        except:
            return False
    
    def get_organization_name(self, obj):
        return obj.organization.user.username