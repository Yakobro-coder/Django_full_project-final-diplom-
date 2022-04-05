from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_up', views.sign_up, name='sign_up'),
]
