from django.urls import path
from .views import (
    GoogleSocialAuthView,
    FacebookSocialAuthView,
    TwitterSocialAuthView,
)


urlpatterns = [
    path("google/", GoogleSocialAuthView.as_view(), name="google"),
    path("facebook/", FacebookSocialAuthView.as_view(), name="facebook"),
    path("twitter/", TwitterSocialAuthView.as_view(), name="twitter"),
]
