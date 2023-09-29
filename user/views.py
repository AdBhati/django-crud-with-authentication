from django.shortcuts import render
from user.models import User
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email","password",
            )

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User


    def create(self, request):
        existing_user = User.objects.filter(email=request.data.get('email'))
        if existing_user:
            return Response("User Already Exists")
        password = request.data['password']
        hashed_password = make_password(password)
        request.data['password'] = hashed_password
        print("password==>",hashed_password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
#-------------------------------------------

    def login(self, request): 
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            print("email===>",email)
            password = serializer.data['password']
            print("password==>",password)
            user = User.objects.filter(email=email).first()
            print("user====>",user)
        if user and check_password (user.password, password):
            print("user password",user.password)
            return Response("Invalid Credentials")
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        return Response(serializer.errors)
        
#-------------------------------------------

    # def login(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # user = User.objects.filter(email=request.data['email'], password= request.data['password'])
    #         email = serializer.data['email']
    #         print("email===>",email)
    #         password = serializer.data['password']
    #         user = authenticate(email=email, password=password)
    #         if user is None:
    #             return Response("Invalid Credentials")
    #         refresh = RefreshToken.for_user(user)
    #         return Response({
    #             'refresh': str(refresh),
    #             'access': str(refresh.access_token),
    #         }) 
    #     return Response(serializer.errors)


    def view_all(self, request):
        userData = User.objects.all()
    #    userData = User.objects.filter(name = request.GET.get("name"))
        serializer = UserSerializer(userData, many=True).data
        return Response(serializer)

    def view_by_id(self, request, pk):
        userData = User.objects.get(pk=pk)
        serializer = UserSerializer(userData).data
        return Response(serializer)

    def partial_update(self, request, pk):
        user = User.objects.get(pk=pk)
        if not user:
            return Response( 'User not found.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





