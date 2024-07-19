from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = User
        #fields = '__all__'      # Eğer bütün alanlarını görek ve apide istek attığında görmek istersek açabilriz exclude kapatarak.
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions']
