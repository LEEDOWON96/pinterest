from django.db import models


# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # 프로젝트 선택 창 이름 변경
    def __str__(self):
        return f'({self.pk}) {self.title}'