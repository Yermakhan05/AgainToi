from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .serializers import UserSerializer, UserProfileSerializer
from .models import User, UserProfile
import jwt, datetime



class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "jwt": token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])

        serializer = UserSerializer(user)
        return Response(serializer.data)
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message" : "succesfully logged out!"
        }
        return response






class UserProfileView(APIView):
    def get(self, request, user_id):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        if payload['id'] != user_id:
            raise AuthenticationFailed('Invalid user')

        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)

        # Передача данных в шаблон
        context = {
            'user': user,
            'user_profile': user_profile
        }
        return render(request, 'profile.html', context)

    def post(self, request, user_id):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        if payload['id'] != user_id:
            raise AuthenticationFailed('Invalid user')

        user_profile = UserProfile.objects.get(user_id=user_id)
        user_profile.phone = request.data.get('phone')
        user_profile.address = request.data.get('address')
        user_profile.save()

        return redirect(f'/profile/{user_id}/')

