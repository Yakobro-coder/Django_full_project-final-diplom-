from .models import Users
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'type', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts']
