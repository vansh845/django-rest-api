from django.urls import path
from .views import getAuthors,getBooks,getAuthor,getBook,createAuthor

urlpatterns = [
    path('authors',getAuthors),
    path('books',getBooks),
    path('author/<int:pk>',getAuthor),
    path('book/<int:pk>',getBook),
    path('create-author',createAuthor)
]