from rest_framework import serializers
from rest_framework.serializers import StringRelatedField
from rest_framework import serializers
from .models import Author, Article, Book, Biography


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

# class SimpleAuthorModelSerializer(ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#         # fields = ['first_name', 'last_name']
#
# class AuthorModelSerializer(ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'


# class BiographyModelSerializer(ModelSerializer):
#     author = SimpleAuthorModelSerializer()
#
#     class Meta:
#         model = Biography
#         fields = '__all__'
#         # exclude = ['text']
#
#
# class ArticleModelSerializer(ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

# class BookModelSerializer(ModelSerializer):
#     authors = StringRelatedField(many=True)
#     # authors = SimpleAuthorModelSerializer(many=True)
#
#     class Meta:
#         model = Book
#         fields = '__all__'
