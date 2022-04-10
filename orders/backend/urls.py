from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

from .views import RegisterUsersViewSet

r = DefaultRouter()
r.register('register', RegisterUsersViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_up', views.sign_up, name='sign_up'),
] + r.urls
