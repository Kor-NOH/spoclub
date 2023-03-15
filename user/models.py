from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=30)          # 실명
    id = models.TextField(primary_key=True)         # 아이디
    pw = models.TextField()                         # 비밀 번호
    phonenum = models.CharField(max_length=30)   # 전화 번호
    age = models.IntegerField(null=True)        # 나이