from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView


from rest_framework.routers import DefaultRouter
from authors.views import AuthorViewSet, BookViewSet
from userapp.views import UserListAPIView
from users.views import UsersModelViewSet
from notes.views import ProjectModelViewSet, NotesModelViewSet
from rest_framework.authtoken import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title='Service',
        default_version='1',
        description='Documentation to out project',
        contact=openapi.Contact(email='admin@admin.com'),
        license=openapi.License(name='MIT License'),
    ),
    # public=True,
    # permission_classes=[permissions.AllowAny],
)





router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
# router.register('biography', BiographyViewSet)
# router.register('articles', ArticleViewSet)

# router_users = DefaultRouter()
# router.register('users', UsersModelViewSet)

# router_notes = DefaultRouter()
# router.register('project', ProjectModelViewSet)
# router.register('notes', NotesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/(?P<version>\d)/users/$', UserListAPIView.as_view()),
    # path('api/authors/', AuthorViewSet.as_view)
    # path('api/users/1', include('userapp.urls', namespace='1')),
    # path('api/users/2/', include('userapp.urls', namespace='2'))
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
