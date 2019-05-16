from django.urls import path, include


urlpatterns = [
    path('users/', include(('user.urls', 'user'))),
    path('posts/', include(('post.urls', 'post'))),
]
