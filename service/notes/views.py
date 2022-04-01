from rest_framework.viewsets import ModelViewSet
from .models import Project, Notes
from .serializers import ProjectModelSerializer, NotesModelSerializer


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer


class NotesModelViewSet(ModelViewSet):
   queryset = Notes.objects.all()
   serializer_class = NotesModelSerializer