from django.urls import include, path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user', views.UserViewSet, basename='user')
router.register(r'post', views.PostViewSet, basename='post')
router.register(r'company', views.PostViewSet, basename='company')


urlpatterns = [
    path('', include(router.urls)),
]