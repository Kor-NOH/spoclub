from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Main(APIView):
    def get(self, request):

        id = request.session['id']
        user = User.objects.filter(id=id).first()

        try:
            if id is None:
                return render(request, "swlab/unknow_user_main.html")

            if user is None:
                return render(request, "login")

        except KeyError:
            return Response({'message': "KEY_ERROR"}, status=400)

        return render(request, "swlab/main.html", context=dict(user=user))


class Register(APIView):
    def get(self, request):
        return render(request, "swlab/register.html")

    def post(self, request):
        name = request.data.get('name', None)
        id = request.data.get('id', None)
        pw = request.data.get('pw', None)
        pw_again = request.data.get('pw_again', None)
        phonenum = request.data.get('phonenum', None)
        schoolssn = request.data.get('schoolssn', None)
        try:
            # 이름(실명) 입력이 공백일 때
            if name == '':
                messages.info(request, '이름(실명)을 입력해주세요.')
                return Response( status=400)
            # 아이디 입력이 공백일 때
            if id == '':
                messages.info(request, '아이디를 입력해주세요.')
                return Response(status=400)
            # 비밀번호 입력이 공백일 때
            if pw == '':
                messages.info(request, '비밀번호를 입력해주세요.')
                return Response(status=400)
            # 비밀번호 확인 입력이 공백일 때
            if pw_again == '':
                messages.info(request, '비밀번호 확인을 입력해주세요.')
                return Response(status=400)
            # 학번 입력이 공백일 때
            if schoolssn == '':
                messages.info(request, '학번 입력해주세요.')
                return Response(status=400)
            # 전화번호 입력이 공백일 때
            if phonenum == '':
                messages.info(request, '전화번호를 입력해주세요.')
                return Response(status=400)
            # 아이디 중복일 때
            if User.objects.filter(id=id).exists():
                messages.info(request, '이미 가입된 아이디입니다.')
                return Response(status=400)
            # 학번 중복일 때
            if User.objects.filter(schoolssn=schoolssn).exists():
                messages.info(request, '이미 가입된 학번입니다.')
                return Response(status=400)
            # 전화번호 중복일 때
            if User.objects.filter(phonenum=phonenum).exists():
                messages.info(request, '이미 가입된 전화번호입니다.')
                return Response(status=400)
            # 비밀번호 입력과 확인이 다를 때
            if pw_again != pw:
                messages.info(request, '비밀번호가 동일하지 않습니다.')
                return Response(status=400)
            # 비밀번호 8~20 자리가 아닐 때
            if len(pw) < 8 or len(pw) > 20:
                messages.info(request, '비밀번호가 8~20자리가 아닙니다.')
                return Response(status=400)

        # 키 에러
        except KeyError:
            return Response({'message': "KEY_ERROR"}, status=400)
        User.objects.create(name=name,
                            id=id,
                            pw=make_password(pw),
                            phonenum=phonenum,
                            schoolssn=schoolssn)
        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "swlab/login.html")

    def post(self, request):
        id = request.data.get('id', None)
        pw = request.data.get('pw', None)
        CHuser = User.objects.filter(id=id).first()

        if CHuser is None:
            print("wrong id")
            return Response(status=400)
        else:
            if CHuser.pw == pw:
                print("correct your id,pw")
                request.session['id'] = id
                return Response(status=200)
            else:
                print("wrong pw")
                return Response(status=400)

class Profile(APIView):
    def get(self, request):

        id = request.session['id']

        if id is None:
            return render(request, "login")

        user = User.objects.filter(id=id).first()

        if user is None:
            return render(request, "login")

        return render(request, "swlab/profile.html", context=dict(users=user))

class Logout(APIView):
    def get(self, request):
        request.session.flush() # 계정 정보 세션 삭제
        return render(request, "swlab/login.html")

class Unknow_user_main(APIView):
    def get(self, request):
        return render(request, "swlab/unknow_user_main.html")
