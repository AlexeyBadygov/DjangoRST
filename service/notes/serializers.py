from rest_framework.serializers import ModelSerializer
from .models import Notes


class NotesModelSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'