from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
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

class BlogPage(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blogs.html"

class BlogDetailPage(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog_details.html"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ["title", 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # sets author before we validate

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields = ['title', 'body']

    def test_func(self): #
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
