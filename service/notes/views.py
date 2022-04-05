from django.db.migrations import serializer
from rest_framework import mixins, viewsets
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


class NotesModelViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer

    # def del_queryset(self):
    #     active = self.request.query_params.get('active')
    #     notes = Notes.objects.all()
    #     if active:
    #             active = False
    #     return active


class NotestLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
