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

class SoccerTeam(models.Model):
    stname = models.TextField(max_length=10)    # 축구 팀 이름
    sport_type = models.TextField(max_length=20)    # 스포츠 종목
    open_date = timestamp(null = False)     # 생성 날짜