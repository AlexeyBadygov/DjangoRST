import graphene
from graphene_django import DjangoObjectType

from authors.models import Book, Author
from notes.models import Project, Notes
from users.models import Users


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class ProjecType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = Notes
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = Users
        fields = "__all__"


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    all_project = graphene.List(ProjecType)
    all_notes = graphene.List(ToDoType)
    all_users = graphene.List(UserType)

    user_by_project = graphene.Field(UserType, id=graphene.Int(required=True))


    def resolve_user_by_project(self, info, id):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExist:
            return None


    def resolve_all_books(self, info):
        return Book.objects.all()


    def resolve_all_authors(self,info):
        return Author.objects.all()


    def resolve_all_project(self, info):
        return Project.objects.all()


    def resolve_all_notes(self, info):
        return Notes.objects.all()


    def resolve_all_users(self, info):
        return Users.objects.all()


schema = graphene.Schema(query=Query)
