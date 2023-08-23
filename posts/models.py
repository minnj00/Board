from django.db import models


# 만약 model 안의 이름이 무언가가 바뀌면 다시 번역 코드를 입력해야함.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)