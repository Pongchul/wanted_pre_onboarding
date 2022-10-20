from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from api import serializers
from api.models import User, Post, Company


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializers_class = serializers.CompanySerializer


class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializers_class = serializers.PostCreatedSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.PostCreatedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = serializers.PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = serializers.PostRetrieveSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)

        serializer = serializers.PostUpdateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



