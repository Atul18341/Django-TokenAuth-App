from django.urls import path
from .views import Helloview
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
     path("hello/",Helloview.as_view(),name="hello"),
     path("",obtain_auth_token,name="api_token_auth"),
]