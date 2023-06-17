from rest_framework import serializers
from books.models import Book, Chapter


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'created_at', 'modified_at']


class ChapterSerializer(serializers.ModelSerializer):
    character_number = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Chapter
        fields = ['id', 'book','content','title', 'created_at', 'modified_at',"character_number"]

    def get_character_number(self,instance):
        return len(instance.content)