from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Swagger
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
# from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import redirect

# GenericAPIView
from rest_framework import generics

from guestbook.models import *
from .serializers import *
import json
import datetime

# Create your views here.

# 방명록 작성 기능
# 제목, 작성자, 내용, 게시글 비밀번호 입력받기
# 방명록 삭제 기능
# 올바른 게시글 비밀번호를 입력하면 삭제 가능
class GuestBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kargs):
        instance = self.get_object()
        password = request.data.get('password')

        if password == instance.password:
            self.perform_destroy(instance)
            return Response({"message":"삭제가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error":"잘못된 비밀번호 입니다."}, status=status.HTTP_403_FORBIDDEN)


# 방명록 리스트 기능
# 방명록 보여주기
# class GuestBookList(generics.ListAPIView):
#     queryset = GuestBook.objects.all()
#     serializer_class = GuestBookSerializer

# 방명록 시간 순 정렬
class GuestBookList(generics.ListCreateAPIView):
    serializer_class = GuestBookSerializer

    def get_queryset(self):
        return GuestBook.objects.order_by('-created_at')