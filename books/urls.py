from django.urls import path

from . import views


urlpatterns = [
    path('book', views.BookListView.as_view(), name='book-list'),
    path('book/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author', views.AuthorListView.as_view(), name='author-list'),
    path('author/<slug:slug>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
