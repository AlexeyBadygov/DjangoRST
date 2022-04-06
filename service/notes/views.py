from django.db.migrations import serializer
from rest_framework import mixins, viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, Notes
from .serializers import ProjectModelSerializer, NotesModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        return Project.objects.filter(name__contains='часть_имени_проекта')

    class ProjectLimitOffsetPagination(LimitOffsetPagination):
        default_limit = 10


class NotesModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer


class NotesModelViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.active('False')


class NotestLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
