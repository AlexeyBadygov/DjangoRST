from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet
from users.views import UsersModelViewSet
from notes.views import ProjectModelViewSet, NotesModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('articles', ArticleModelViewSet)

router_users = DefaultRouter()
router_users.register('users', UsersModelViewSet)

router_notes = DefaultRouter()
router_notes.register('project', ProjectModelViewSet)
router_notes.register('notes', NotesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('users/', include(router_users.urls)),
    path('notes/', include(router_notes.urls))
]
