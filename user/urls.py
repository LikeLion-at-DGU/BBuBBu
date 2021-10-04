from django.urls import path
from .views import *

app_name="user"
urlpatterns = [
    path('login',login_view, name='login'),
    path('signup/',signup_view,name='signup'),
    path("main/", main, name='main'),
] 
