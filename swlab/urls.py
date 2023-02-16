# from django.contrib import admin
from django.urls import path
from .views import Main, Register, Login, Profile, Logout, Unknow_user_main, Change_pw

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('main', Main.as_view()),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('profile', Profile.as_view()),
    path('logout', Logout.as_view()),
    path('unknow_user_main', Unknow_user_main.as_view()),
    path('change_pw', Change_pw.as_view())
]
