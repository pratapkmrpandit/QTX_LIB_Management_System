from rest_framework import viewsets , filters
from rest_framework.pagination import PageNumberPagination
from .models import Library , Author , Category , Book , Borrowing , Member , Review
from .serializers import (
    librarySerializer,
    authorSerializer,
    categorySerializer,
    borrowingSerializer,
    bookSerializer,
    memberSerializer,
    reviewSerializer,
)

class standardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('name')
    serializer_class = librarySerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name','campus_location']
    ordering_fields = ['name','created_on']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = authorSerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','nationality']
    ordering_fields = ['first_name','last_name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = categorySerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name','description']
    ordering_fields = ['name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = bookSerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter , filters.OrderingFilter]
    search_fields = ['title','isbn']
    ordering_fields = ['title','publication_date','available_copies']

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('first_name')
    serializer_class = memberSerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','email']
    ordering_fields = ['first_name','last_name','registration_date']

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all().order_by('-borrow_date')
    serializer_class = borrowingSerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["book__title", "member__first_name", "member__last_name"]
    ordering_fields = ["borrow_date", "due_date", "return_date"]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-review_date')
    serializer_class = reviewSerializer
    pagination_class = standardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["book__title", "member__first_name", "comment"]
    ordering_fields = ["rating", "review_date"]