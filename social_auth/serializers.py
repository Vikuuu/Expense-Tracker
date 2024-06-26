from rest_framework import serializers
from . import google, facebook, twitterhelper
import os
from rest_framework.exceptions import AuthenticationFailed
from .register import register_social_user


class GoogleSocailAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        if user_data["aud"] != os.getenv("GOOGLE_CLIENT_ID"):
            raise AuthenticationFailed("oops, who are you?")

        user_id = user_data["sub"]
        email = user_data["email"]
        name = user_data["name"]
        provider = "google"

        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name,
        )


class FacebookSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        try:
            user_id = user_data["id"]
            email = user_data["email"]
            name = user_data["name"]
            provider = "facebook"

            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name,
            )
        except Exception as identifier:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )


class TwitterSocialAuthSerializer(serializers.Serializer):
    access_token_key = serializers.CharField()
    access_token_secret = serializers.CharField()

    def validate(self, attrs):
        access_token_key = attrs.get("access_token_key")
        access_token_secret = attrs.get("access_token_secret")

        user_info = (
            twitterhelper.TwitterAuthTokenVerification.validate_twitter_auth_token(
                access_token_key, access_token_secret
            )
        )
        try:
            user_id = user_info["id_str"]
            email = user_info["email"]
            name = user_info["name"]
            provider = "twitter"
        except:
            raise serializers.ValidationError(
                "The tokens are invalid or expired. Please login again."
            )
        
        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name,
        )
