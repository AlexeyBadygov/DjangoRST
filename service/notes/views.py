from django.db.migrations import serializer
from rest_framework import mixins, viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Notes
from .serializers import NotesModelSerializer


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
