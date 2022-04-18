from rest_framework import views, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer, \
    SimpleAuthorModelSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import mixins



# class AuthorApiView(ListAPIView, CreateAPIView):
#    renderer_classes = [JSONRenderer]
#    queryset = Author.objects.all()
#    serializer_class = AuthorModelSerializer


# class AuthorModelView(
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     GenericViewSet
# ):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#
# class AuthorApiView(viewsets.ViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer


    # @action(detail=True, methods=['get'])
    # def change_password(self, request):
    #     return Response('dsdsdsd')

    #
    # def list(self, request):
    #     authors = Author.objects.all()
    #     serializer = AuthorModelSerializer(authors, many=True)
    #     return Response(serializer.data)


class AuthorModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = ['StaticHTMLRender']
    queryset = Author.objects.all()
    serializer_class = SimpleAuthorModelSerializer
    # filter_fields = ['first_name']


    # def get_queryset(self):
    #     # param = self.request.headers.get('param')
    #     # return Author.objects.filter(first_name__contains=param)
    #
    #     param = self.kwargs['name']
    #     return Author.objects.filter(first_name__contains=param)


class BookModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer
