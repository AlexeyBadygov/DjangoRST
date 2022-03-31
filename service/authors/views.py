from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer


class AuthorModelViewSet(ModelViewSet):
   # renderer_classes = ['StaticHTMLRender']
   queryset = Author.objects.all()
   serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
   queryset = Biography.objects.all()
   serializer_class = BiographyModelSerializer
