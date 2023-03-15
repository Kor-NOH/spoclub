from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Main(APIView):
    def get(self, request):

        id = request.session.get('id', None)

        if id is None:
            return render(request, "swlab/unknow_user_main.html")

        user = User.objects.filter(id=id).first()

        if user is None:
            return render(request, "swlab/unknow_user_main.html")

        # 접속하기 버튼을 눌렀을때
        # if id_insert, pw_insert = id, pw:     //아이디 비번 재입력하고 그게 원래 계정이랑 맞다면
        #     os.popen("ssh 22port")    // 22포트로 접근

        #     if 사용자명/ssh 폴더가 있으면 : // 사용자에 맞는 키가 있는지 없는지 확인
        #            os.popen("ssh 사용자명/ssh키폴더/8022port") // 키로 8022포트 접속

        #     else: //키가 없다면
        #            os.popen("keygen") //본인 키 생성
        #            os.changedirectory // 본인 키의 디렉토리명 변경
        #            os.popen("ssh 사용자명/ssh키폴더/8022port") // 키로 8022포트 접속

        #           ------------------------02.23 변경사항--------------------------------
        #           -------api는 두고 DCUCODE 디비랑 연동하기로 해서 웹에서 ssh 띄우기 용--------
        #            os.checkIP //본인에게 할당받은 파드의 포트번호를 확인
        #            mv.url("yourselfIP")   // url을 본인이 할당받은 아이피로 변경 후 접속
        #           ---------------------------------------------------------------------

        # else: // 재입력한 아이디 비번이 다르다면
        #     error("아이디 비번 틀림")    // 경고문과 동시에 아이디,비번 재입력

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
        age = request.data.get('age', None)
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
            # 나이 입력이 공백일 때
            if age == '':
                messages.info(request, '나이를 입력해주세요.')
                return Response(status=400)
            # 전화번호 입력이 공백일 때
            if phonenum == '':
                messages.info(request, '전화번호를 입력해주세요.')
                return Response(status=400)
            # 아이디 중복일 때
            if User.objects.filter(id=id).exists():
                messages.info(request, '이미 가입된 아이디입니다.')
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
                            age=age)

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "swlab/login.html")

    def post(self, request):
        id = request.data.get('id', None)
        pw = request.data.get('pw', None)
        CHuser = User.objects.filter(id=id).first()
        user = User.objects.get(id=id)

        if CHuser is None:
            print("wrong id")
            return Response(status=400)
        else:
            if check_password(pw, user.pw):
                print("correct your id,pw")
                request.session['id'] = id
                return Response(status=200)
            else:
                print("wrong pw")
                return Response(status=400)

class Profile(APIView):
    def get(self, request):

        id = request.session.get('id', None)

        if id is None:
            return render(request, "swlab/unknow_user_main.html")

        user = User.objects.filter(id=id).first()

        if user is None:
            return render(request, "swlab/unknow_user_main.html")

        return render(request, "swlab/profile.html", context=dict(users=user))

class Logout(APIView):
    def get(self, request):
        request.session.flush() # 계정 정보 세션 삭제
        return render(request, "swlab/login.html")

class Unknow_user_main(APIView):
    def get(self, request):
        return render(request, "swlab/unknow_user_main.html")

class Change_pw(APIView):
    def get(self, request):

        id = request.session.get('id', None)
        if id is None:
            return render(request, "swlab/unknow_user_main.html")

        user = User.objects.filter(id=id).first()
        if user is None:
            return render(request, "swlab/unknow_user_main.html")

        return render(request, "swlab/change_pw.html", context=dict(users=user))

    def post(self, request):

        oldpw = request.data.get('oldpw', None)
        newpw = request.data.get('newpw', None)
        chnewpw = request.data.get('chnewpw', None)

        try:
            # 이전 비밀번호가 공백일 때
            if oldpw == '':
                messages.info(request, '이전 비밀번호를 입력해주세요.')
                return Response(status=400)
            # 새 비밀번호가 공백일 때
            if newpw == '':
                messages.info(request, '(새 비밀번호를 입력해주세요.')
                return Response(status=400)

            # 새 비밀번호 확인이 공백일 때
            if chnewpw == '':
                messages.info(request, '새 비밀번호 확인을 입력해주세요.')
                return Response(status=400)

        except KeyError:
            return Response({'message': "KEY_ERROR"}, status=400)

        return Response(status=200)
