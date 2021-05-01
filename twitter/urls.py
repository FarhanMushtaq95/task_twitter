from django.urls import path
from django.conf.urls import url
from .views import *

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    url(r'^profile', UserProfileView.as_view()),
    url(r'^new_post', Post.as_view()),

    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),

]