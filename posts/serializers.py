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
    redactor_name = serializers.SerializerMethodField()
    redactor_url = serializers.SerializerMethodField()
    redactor_telegram = serializers.SerializerMethodField()
    redactor_youtube = serializers.SerializerMethodField()
    redactor_instagram = serializers.SerializerMethodField()
    redactor_facebook = serializers.SerializerMethodField()

    
    class Meta:
        model = Post
        fields = ['url', 'id', 'text', 'date', 'number_of_likes', 
                  'liked_by_user', 'is_favourite', 'redactor_name',
                  'redactor_url', 'redactor_youtube', 'redactor_instagram', 'redactor_facebook', 'redactor_telegram','redactor', 'post_likes', 'comments']

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
    
    def get_redactor_name(self, obj):
        return obj.redactor.user.username
    
    def get_redactor_url(self, obj):
        redactor_id = obj.redactor.id
        return f"http://127.0.0.1:8000/redactor/{redactor_id}"
    
    def get_redactor_instagram(self, obj):
        return obj.redactor.instagram
    
    def get_redactor_telegram(self, obj):
        return obj.redactor.telegram
    
    def get_redactor_youtube(self, obj):
        return obj.redactor.youtube
    
    def get_redactor_facebook(self, obj):
        return obj.redactor.facebook