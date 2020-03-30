from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ..serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request):
        return Response({ 'he': True })

    def create(self, request):
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(data=request.data, context=serializer_context)

        if (serializer.is_valid()):
            user = User.objects.create_user(**request.data)
            return Response(request.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
