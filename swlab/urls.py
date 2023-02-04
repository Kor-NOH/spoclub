from django.contrib import admin
from django.urls import path
from .views import Sub, Register, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Sub.as_view()),
    path('register', Register.as_view()),
    path('login', Login.as_view())
]
