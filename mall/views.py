from django.contrib.auth.models import User
from rest_framework import viewsets

from mall.serializers import UserSerializer

from mall.models import Product, Bid
from mall.serializers import ProductsSerializer, BidsSerializer

from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class BidsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Bid.objects.all()
    serializer_class = BidsSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['value', 'date_published', 'placer', 'product']
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(placer=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'category', 'condition', 'brand', 'starting_price', 'deadline', 'owner', 'max_bid']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
