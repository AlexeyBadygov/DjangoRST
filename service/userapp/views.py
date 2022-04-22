from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithFullName


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        print(self.request.version)
        if self.request.version == '1':
            return UserSerializerWithFullName
        return UserSerializer
