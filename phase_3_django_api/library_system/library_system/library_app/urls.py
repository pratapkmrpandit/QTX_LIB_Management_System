from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter

from .views import (
    LibraryViewSet,
    AuthorViewSet,
    CategoryViewSet,
    BookViewSet,
    MemberViewSet,
    BorrowingViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r"libraries", LibraryViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"books", BookViewSet)
router.register(r"members", MemberViewSet)
router.register(r"borrowings", BorrowingViewSet)
router.register(r"reviews", ReviewViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
