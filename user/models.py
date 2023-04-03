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
    team_mark = models.ImageField(null=True)    # 팀 마크
    team_intro = models.TextField(max_length=200)   # 팀 소개글

class TeamRealation(models.Model):
    sportevent = models.TextField(max_length=20) # 종목
    teamname = models.ForeignKey('SpoTeam', on_delete=models.CASCADE, db_column='teamname') # 팀 이름
    username = models.TextField(max_length=10)    # 소속 유저 이름
    userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userid')    # 소속 유저 아이디
    position = models.TextField(max_length=20)  # 포지션
    manager = models.BooleanField(default=False)    # 관리자인가?
    rank = models.TextField(max_length=20)  # 직급