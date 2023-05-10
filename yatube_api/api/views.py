from rest_framework import filters

from django.shortcuts import get_object_or_404

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import (CustumCreateListViewSet, CustumModelViewSet,
                       CustumReadOnlyModelViewSet)

from posts.models import Group, Post  # isort:skip


class CommentViewSet(CustumModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get("post_id")),
        )


class GroupViewSet(CustumReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CustumCreateListViewSet):
    serializer_class = FollowSerializer
    search_fields = ("=following__username", "=user__username")
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(CustumModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
