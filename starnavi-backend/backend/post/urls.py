from django.urls import path

from . import views

urlpatterns = [
    path('create', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/like', views.PostLikeView.as_view(), name='like'),
]
