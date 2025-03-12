from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author,Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.

@api_view(['GET'])
def getAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAuthor(request,pk):
    author = Author.objects.filter(pk=pk).first()
    serializer = AuthorSerializer(author)

    return Response(serializer.data)
    
@api_view(['POST'])
def createAuthor(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request,pk):
    book = Book.objects.filter(pk=pk).first()
    serializer = BookSerializer(book)

    return Response(serializer.data)