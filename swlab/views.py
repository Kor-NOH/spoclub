from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib import messages


class Sub(APIView):
    def get(self, request):
        return render(request, "swlab/main.html")


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
            if name == '':
                messages.info(request, '이름(실명)을 입력해주세요.')
                return Response( status=400)
            if id == '':
                messages.info(request, '아이디를 입력해주세요.')
                return Response(status=400)
            if pw == '':
                messages.info(request, '비밀번호를 입력해주세요.')
                return Response(status=400)
            if pw_again == '':
                messages.info(request, '비밀번호 확인을 입력해주세요.')
                return Response(status=400)
            if schoolssn == '':
                messages.info(request, '학번 입력해주세요.')
                return Response(status=400)
            if phonenum == '':
                messages.info(request, '전화번호를 입력해주세요.')
                return Response(status=400)

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

        user = User.objects.filter(id=id).first()
        if user is None:
            print("wrong id")
            return Response(status=400)
        else:
            if user.pw == pw:
                print("correct your id,pw")
                return Response(status=200)
            else:
                print("wrong pw")
                return Response(status=400)

class Profile(APIView):
    def get(self, request):
        user_list = User.objects.all()

        return render(request, "swlab/profile.html", context=dict(users=user_list))

class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "swlab/login.html")
