from rest_framework import mixins, pagination, permissions, viewsets

from .permissions import AuthorReadOnly


class CustumCreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    permission_classes = (permissions.IsAuthenticated, AuthorReadOnly)
    pagination_class = pagination.LimitOffsetPagination


class CustumReadOnlyModelViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorReadOnly,
    )
    pagination_class = pagination.LimitOffsetPagination


class CustumModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorReadOnly,
    )
    pagination_class = pagination.LimitOffsetPagination
