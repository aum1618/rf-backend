from django.urls import path
from .views import (
    welcome,
    RetrieveBlogs,
    RetrieveFAQS,
    SignupView,
    LoginView,
    UserDetailView,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", welcome, name="welcome"),
    path("blogs", RetrieveBlogs.as_view(), name="blogs"),
    path("faqs", RetrieveFAQS.as_view(), name="faqs"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("user-detail/", UserDetailView.as_view(), name="user-detail"),
]
