from django.shortcuts import render
from rest_framework import viewsets
from posts.serializers import (PostSerializer, Post_likeSerializer, CommentSerializer,
                               FavouriteSerializer, Comment_answerSerializer, Comment_likeSerializer)
from posts.models import (Post, Post_like, Comment, Favourite, 
                          Comment_answer, Comment_like)