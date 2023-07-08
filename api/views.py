from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from blog.serializers import BlogSerializer
from blog.models import Blog
from faq.models import FAQ
from faq.serializers import FAQSerializer
from django.contrib.auth import authenticate
from rest_framework import status, views
from rest_framework.response import Response

# from user.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# class UserDetailView(views.APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)


# class SignupView(views.APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(user.password)
#             user.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(views.APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         else:
#             return Response(
#                 {"error": "Wrong username or password."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to RENDITEFUCHS")


class RetrieveBlogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class RetrieveFAQS(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
