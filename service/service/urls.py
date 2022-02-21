from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from users.views import UsersModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

router_users = DefaultRouter()
router_users.register('users', UsersModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('users/', include(router_users.urls))

]
