from rest_framework import status, views, viewsets, generics
from rest_framework.response import Response
from .serializers import PostCreateSerializer, PostLikeSerializer
from .models import Post


class PostCreateView(generics.CreateAPIView):
    """
    POST post/create
    :param user_id
    :param title
    :param description
    """

    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostLikeView(generics.GenericAPIView):
    """
    POST post/<int>/like
    :param id

    DELETE post/<int>/like
    :param id
    """

    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.kwargs)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            post = self.get_object()
            if user not in post.likes.all():
                post.likes.add(user)
                return Response()
            return Response({'message': 'User has already liked this post.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.kwargs)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            post = self.get_object()
            if user in post.likes.all():
                post.likes.remove(user)
                return Response()
            return Response({'message': 'User did not like this post.'},
                            status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
