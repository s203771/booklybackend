from django.urls import path
from books.views import BookView, ChapterView, ChapterDetailedView

urlpatterns = [
        path("", BookView.as_view()),
        path("<int:pk>/chapters", ChapterView.as_view()),
        path("<int:pk>/chapters/<int:chapter_id>", ChapterDetailedView.as_view()),
        path("chapters/", ChapterView.as_view()),
        path("chapters/<int:chapter_id>", ChapterView.as_view()),
]
