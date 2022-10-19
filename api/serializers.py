from rest_framework import serializers

from api.models import User, Post, Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PostCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    company_country = serializers.CharField(source='company.country')
    company_location = serializers.CharField(source='company.city')

    class Meta:
        model = Post
        fields = ['id','position','compensation','skill',
                  'company_name', 'company_country', 'company_location']


class PostRetrieveSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    company_country = serializers.CharField(source='company.country')
    company_location = serializers.CharField(source='company.city')

    class Meta:
        model = Post
        fields = ['id','position','compensation','skill','description',
                  'company_name', 'company_country', 'company_location']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['position','compensation','description','skill']