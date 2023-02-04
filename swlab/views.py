from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password
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
