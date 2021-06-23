from django.contrib import auth
from django.http.response import HttpResponse
from rest_framework.response import Response
from basic.serializer import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def loginApi(request, username, password):
    if request.user:
        if request.user.is_authenticated:
            auth.logout(request)
            user_var = auth.authenticate(request, username=username, password=password)
            auth.login(request, user_var)

            if request.user.is_authenticated:
                user_data = User.objects.get(username=username)
                user_serializer = UserSerializer(user_data, many=False)
                return Response(user_serializer.data)
            else:
                return HttpResponse('')
        else:
            user_var = auth.authenticate(request, username=username, password=password)
            auth.login(request, user_var)

            if request.user.is_authenticated:
                user_data = User.objects.get(username=username)
                user_serializer = UserSerializer(user_data, many=False)
                return Response(user_serializer.data)
            else:
                return HttpResponse('')
    else:
        return HttpResponse('')