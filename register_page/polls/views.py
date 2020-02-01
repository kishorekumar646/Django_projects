from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.template.loader import render_to_string
from polls.models import Registration
from polls.serializer import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from polls.token import token_activation
from register_page.settings import SECRET_KEY, AUTH_ENDPOINT, JWT_AUTH

import jwt

class login_API(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/home_page/")
        else:
            return Response("Invalid User")

        # return render(request,"login.html")


class register_API(GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        userName = request.POST['user_name']
        email = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['conform_password']

        if password == confirm_password:

            user = User.objects.create_user(
                username=userName, email=email, password=password)
            user.save()
            print("user saved successfully")

            current_site = get_current_site(request)
            domain_name = current_site.domain
            print("current site name : ", current_site)

            token = token_activation(userName, password)
            print("token : ", token)

            url = str(token)
            print("url : ", url)

            surl = get_surl(url)
            print("surl : ", surl)

            z = surl.split("/")
            print("z : ", z)
            print("z[2]", z[2])

            mail_subject = "Click link for activating "
            msg = render_to_string('email_validation.html', {
                'user': user.username,
                'domain': domain_name,
                'surl': z[2]
            })

            recipients = email
            print(msg)
            email = EmailMessage(mail_subject, msg, to=[recipients])
            email.send()

            print('confirmation mail sent')
            return HttpResponse('Please confirm your email address to complete the registration')

            # return redirect("/login-api/")
        else:
            return Response("Password missmatch")

        # return render(request,"register.html")

def activate(request,surl):
    print("Activate url is : ",surl)

    try:
        token_object = ShortURL.objects.get(surl=surl)
        token = token_object.lurl
        decode = jwt.decode(token,SECRET_KEY)
        user_name = decode['username']
        user = User.objects.get(username = user_name)

        if user is not None:
            user.is_active = True
            user.save()
            messages.info(request,"your account is active now")
            return redirect("/login-api/")

        else:
            messages.info(request,"was not able to send email")
            return redirect("/register-api/")

    except KeyError:
        messages.info(request, 'was not able to sent the email')
        return redirect("/register-api/")


def homePage(request):

    return render(request, 'home_page.html')
