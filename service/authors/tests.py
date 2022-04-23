import json


from django.contrib.auth.models import User
from django.test import TestCase
from mixer.backend.django import mixer

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from .models import Author, Book
from .views import AuthorViewSet


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'last_name': 'Пушкин', 'birthday_year': 1799}, format='json')
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_create_admin(self):
       factory = APIRequestFactory()
       request = factory.post('/api/authors/', {'last_name': 'Пушкин', 'birthday_year': 1799}, format='json')
       admin = User.objects.create_superuser('admin', 'admin123@admin.com', 'admin')
       force_authenticate(request, admin)
       view = AuthorViewSet.as_view({'post': 'create'})
       response = view(request)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_detail(self):
        author = Author.objects.create(first_name='Pushkin', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.uuid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_edit_guest(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.put(f'/api/authors/{author.uuid}/', {'last_name':'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(name='Пушкин', birthday_year=1799)
        client = APIClient()
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/authors/{author.uuid}/', {'last_name': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(author.uuid)
        self.assertEqual(author.last_name, 'Грин')
        self.assertEqual(author.birthday_year, 1880)
        client.logout()


# class TestMath(APISimpleTestCase):
#
#     def test_sqrt(self):
#         import math
#         self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        book = Book.objects.create(name='Пиковая дама', author=author)
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и Людмила', 'author': book.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name, 'Руслан и Людмила')


    def test_edit_mixer(self):
        book = mixer.blend(Book)
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

        self.client.login(username='admin', password='admin')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и Людмила', 'author': book.author.uuid})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name, 'Руслан и Людмила')
