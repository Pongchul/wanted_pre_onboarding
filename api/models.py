from django.db import models

# Create your models here.


class Company(models.Model):
    National_Choices = (
        ('KR', '한국'),
        ('JP', '일본'),
        ('CI', '중국'),
        ('US', '미국'),
    )

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=National_Choices)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)



class Post(models.Model):
    company = models.ForeignKey(Company, related_name="company", on_delete=models.CASCADE)

    position = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    compensation = models.IntegerField()
    description = models.TextField()

    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company.name}, {self.position}'


class Apply(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)