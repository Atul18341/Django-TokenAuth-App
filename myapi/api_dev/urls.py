from django.urls import path
from .views import Helloview,signup,signin,home
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
     path("hello/",Helloview.as_view(),name="hello"),
     path("auth",obtain_auth_token,name="api_token_auth"),
     path("",home,name="homepage"),
     path("signup",signup,name="signup"),
     path("login",signin,name="login")
]