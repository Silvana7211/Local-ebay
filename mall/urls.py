from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from mall import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'bids', views.BidsViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
