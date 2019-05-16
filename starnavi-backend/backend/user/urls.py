from django.urls import path

from . import views

urlpatterns = [
    path('auth/signup', views.UserSignUpView.as_view(), name='sign_up'),
    path('auth/login', views.UserLoginView.as_view(), name='login'),
]
