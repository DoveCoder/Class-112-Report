from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.urls import reverse_lazy
from .models import Post

class HomePage(TemplateView):
    template_name = "home.html"

class BlogPage(ListView):
    model = Post
    template_name = "blogs.html"

class BlogDetailPage(DetailView):
    model = Post
    template_name = "blog_details.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ["title", 'body', 'author']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog")
