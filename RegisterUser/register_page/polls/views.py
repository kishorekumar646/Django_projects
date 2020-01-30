from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from polls.models import Registration 
from polls.serializer import RegistrationSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from polls.token import token_activation 


class login_API(GenericAPIView):
    
    serializer_class = LoginSerializer
    def post(self,request):
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home_page/")
        else:
            return Response("Invalid User")
        
        # return render(request,"login.html")

class register_API(GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self,request):
        userName = request.POST['user_name']
        email = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['conform_password']
        
        if password == confirm_password:
            
            user_created = User.objects.create_user(username=userName,email=email,password=password)
            user_created.save()
            
            token = token_activation(userName, password)
            print("token : ",token)

            sub = 'Thank you for registering'
            msg = 'Welcome to the chatApp'
            from_mail = "kishorekumar131646@gmail.com"
            to_list = [user_created.email]
            send_mail(sub, msg, from_mail, to_list, fail_silently=True)

            return redirect("/login-api/")
        else:
            return Response("Password missmatch")

        # return render(request,"register.html")

def homePage(request):

    return render(request,'home_page.html')