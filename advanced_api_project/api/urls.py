from django.urls import path
from .views import BookListCreateAPIView,BooKRetrieveUpdateDestroyAPIView,AuthorListCreateAPIView,AuthorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('book/', BookListCreateAPIView.as_view(),name='book_list'),
    path('author/', AuthorListCreateAPIView.as_view(),name='Author_list'),
    path('book/<title>:title', BooKRetrieveUpdateDestroyAPIView.as_view(),name='book_list'),
    path('author/<name>:name', AuthorRetrieveUpdateDestroyAPIView.as_view(),name='Author_list'),
]