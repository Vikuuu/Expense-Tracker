from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse("email-verify")
        absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi "
            + user.username
            + "\nThank you for registering with Expense Tracker! \nTo complete the registration process and ensure the security of your account, we need to verify your email address.\nPlease click on the following link to verify your account:\n"
            + absurl
            + "\nIf you did not initiate this registration, please disregard this email. \nThank you for choosing Expense Tracker. We look forward to serving you! "
            + "\nBest Regards,"
            + "\nExpense Tracker"
        )

        data = {
            "email_body": email_body,
            "email_subject": "Verify Your Email",
            "to_email": user.email,
        }
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get("token")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload("user_id"))
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_200_OK
            )

        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST
            )
