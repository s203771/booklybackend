from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from books.models import Book, Chapter
from books.serializers import BookSerializer, ChapterSerializer


# Create your views here.

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterView(generics.ListCreateAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.filter(book_id=self.kwargs.get('pk'))


class ChapterDetailedView(generics.RetrieveUpdateAPIView):
    serializer_class = ChapterSerializer

    def get_object(self):
        return get_object_or_404(Chapter, pk=self.kwargs.get('chapter_id'))
