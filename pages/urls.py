from django.urls import path
from .views import (
    HomePage,
    BlogPage,
    BlogDetailPage,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
    )

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailPage.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name="blog_new"),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]