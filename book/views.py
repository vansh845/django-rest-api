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

@api_view(['POST'])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','PUT'])
def updateAuthor(request,pk):
    try:
        author = Author.objects.get(pk=pk)
        if request.method == 'DELETE':
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        if request.method == 'PUT':
            serializer = AuthorSerializer(author,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','PUT'])
def updateBook(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)