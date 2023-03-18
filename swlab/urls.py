# from django.contrib import admin
from django.urls import path
from .views import Main, Register, Login, Profile, Logout, Unknow_user_main, Change_pw, Addimage
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('main', Main.as_view()),
    path('register', Register.as_view()),
    path('', Login.as_view()),
    path('login', Login.as_view()),
    path('profile', Profile.as_view()),
    path('logout', Logout.as_view()),
    path('unknow_user_main', Unknow_user_main.as_view()),
    path('change_pw', Change_pw.as_view()),
    path('addimage', Addimage.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # media 경로 추가