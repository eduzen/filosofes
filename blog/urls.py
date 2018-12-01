from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post', views.PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]
