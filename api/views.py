from django.shortcuts import  get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api import serializers
from api.models import User, Post, Company, Apply


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

        companyNo = post.company.pk
        anotherPosts = Post.objects.filter(company=companyNo).exclude(pk=pk).values_list('pk',flat=True)

        json = JSONRenderer().render(serializer.data)
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


class ApplyViewSet(viewsets.ViewSet):
    queryset = Apply.objects.all()
    serializers_class = serializers.ApplySerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.ApplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Apply.objects.all()
        serializer = serializers.ApplySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Apply.objects.all()
        apply = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ApplySerializer(apply)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Apply.objects.all()
        apply = get_object_or_404(queryset, pk=pk)

        serializer = serializers.ApplySerializer(apply, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Apply.objects.all()
        apply = get_object_or_404(queryset, pk=pk)
        apply.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchKeyWordViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    filter_backends = [filters.SearchFilter]  # settings.py에 DEFAULT_FILTER_BACKENDS 추가
    search_fields = ['company_name','position','skill']