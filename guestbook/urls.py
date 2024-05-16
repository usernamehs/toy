from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User

urlpatterns = [
    # 방명록 생성, 조회, 삭제
    path('<int:pk>/', GuestBookDetail.as_view()),
    # 방명록 리스트 조회
    path('', GuestBookList.as_view()),
]