"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from information.views import (
        BookListView, 
        BookDetailView, 
        BookCreateView, 
        BookUpdateView, 
        BookDeleteView,
        AuthorListView,
        AuthorDetailView,
        AuthorCreateView,
        AuthorUpdateView,
        AuthorDeleteView,
        index
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('accounts/', include('accounts.urls')),
    
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]