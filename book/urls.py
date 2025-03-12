from django.urls import path
from .views import getAuthors,getBooks,getAuthor,getBook,createAuthor,createBook,updateBook,updateAuthor

urlpatterns = [
    path('authors',getAuthors),
    path('books',getBooks),
    path('author/<int:pk>',getAuthor),
    path('book/<int:pk>',getBook),
    path('create-author',createAuthor),
    path('create-book',createBook),
    path('edit-book/<int:pk>',updateBook),
    path('edit-author/<int:pk>',updateAuthor),

]