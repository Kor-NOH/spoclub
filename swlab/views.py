from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response


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
        phonenum = request.data.get('phonenum', None)
        schoolssn = request.data.get('schoolssn', None)

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
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))
        if user.check_password(pw):
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


