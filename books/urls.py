from django.urls import path
from . import views

urlpatterns = [
    path("all_genre/", views.all_genre),
    path("horror/", views.horror_tags_view),
    path("drama/", views.drama_tags_view),
    path("fantasy/", views.fantasy_tags_view),
    path("comedy/", views.comedy_tags_view),
    path("romance/", views.romance_tags_view),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:id>/", views.BookDetailView.as_view()),
    path("books/<int:id>/delete/", views.DeleteBookView.as_view()),
    path("books/<int:id>/update/", views.EditBookView.as_view()),
    path("create_book/", views.CreateBookView.as_view()),
    path("search/", views.SearchView.as_view(), name="search"),
    path("name/", views.name_view),
    path("hobby/", views.hobby_view),
    path("time/", views.times_view),
    path("random/", views.random_view),
]
