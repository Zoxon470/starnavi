import django_rq
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler, \
    jwt_payload_handler

from .serializers import UserSignUpSerializer, UserLoginSerializer
from .tasks import verify_email, find_enrichment
from .models import User


class UserSignUpView(generics.CreateAPIView):
    """
    POST user/signup
    :param email
    :param password
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(**serializer.validated_data)
            django_rq.enqueue(verify_email, user)
            django_rq.enqueue(find_enrichment, user)
            token = jwt_encode_handler(jwt_payload_handler(user))
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(views.APIView):
    """
    POST user/login/
    :param email
    :param password
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(request, **serializer.validated_data)
            if user:
                login(request, user)
                token = jwt_encode_handler(jwt_payload_handler(user))
                return Response({'token': token})
            return Response({'error': 'User is not authorized.'},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
