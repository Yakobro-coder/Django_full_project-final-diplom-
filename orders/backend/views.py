from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Users
from .serializers import UsersSerializer


def home(request):
    return render(request, 'backend/home.html')


def log_in(request):
    return render(request, 'backend/log_in.html')


def sign_up(request):
    return render(request, 'backend/sign_up.html')


class RegisterUsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):
        if {'email', 'password', 'first_name', 'last_name', }.issubset(request.data):
            errors = {}

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
