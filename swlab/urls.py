from django.contrib import admin
from django.urls import path
from .views import Sub, Register, Login, Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',Sub.as_view()),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('profile', Profile.as_view())
]
