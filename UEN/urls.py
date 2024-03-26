"""
URL configuration for UEN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from user.views import (UserViewSet, OrganizationViewSet, VolonteerViewSet)
from posts.views import (PostViewSet, PostLikeViewSet, FavouriteViewSet,
                         CommentViewSet, CommentLikeViewSet, CommentAnswerViewSet,
                         CommentAnswerLikeViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="UEN API",
      default_version='v1',
      description="API for all things …",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'volonteer', VolonteerViewSet)
router.register(r'orgnanization', OrganizationViewSet)
router.register(r'post', PostViewSet)
router.register(r'post_like', PostLikeViewSet)
router.register(r'favourite', FavouriteViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'comment_like', CommentLikeViewSet)
router.register(r'comment_answer', CommentAnswerViewSet)
router.register(r'comment_answer_like', CommentAnswerLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
