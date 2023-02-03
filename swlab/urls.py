from django.contrib import admin
from django.urls import path
from .views import Sub, Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Sub.as_view()),
    path('register', Register.as_view())
]
