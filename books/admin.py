from django.contrib import admin

from books.models import Book,Chapter


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass
