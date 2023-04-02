import timestamp as timestamp
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=30)          # 실명
    id = models.TextField(primary_key=True)         # 아이디
    pw = models.TextField()                         # 비밀 번호
    phonenum = models.CharField(max_length=30)   # 전화 번호
    age = models.IntegerField(null=True)        # 나이

class Images(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가

class SpoTeam(models.Model):
    sportevent = models.TextField(max_length=20)    # 종목
    name = models.TextField(primary_key=True, max_length=20)    # 팀 이름
    created_at = models.DateTimeField(auto_now_add=True)    # 팀 생성 시간
    team_mark = models.ImageField(null=True)
    team_intro = models.TextField(max_length=200)   # 팀 소개글