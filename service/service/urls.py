from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet
from users.views import UsersModelViewSet
from newapp.views import ProjectModelViewSet, NotesModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('articles', ArticleModelViewSet)

router_users = DefaultRouter()
router_users.register('users', UsersModelViewSet)

router_project = DefaultRouter()
router_project.register('project', ProjectModelViewSet)
router_project.register('notes', NotesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('users/', include(router_users.urls))

]
