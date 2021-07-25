from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article',
                               null=True)  # 회원탈퇴한 게시글일 때 게시글을 보존하되 writer->null

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
