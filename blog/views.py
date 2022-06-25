from sre_constants import SUCCESS
from django.shortcuts import render
from django.views import generic
from django.views import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Create your views here.


class PostListView(generic.ListView):
    model = Post

    class PostCreateView(generic.CreateView):
        model = Post
        fields = ['all']
        sucess_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

    class PostUpdateView(generic.UpdateView):
        model = Post
        fields = ['all']
        sucess_url = reverse_lazy("blog:all")

    class PostDeleteView(generic.DeleteView):
        model = Post
        fields = ['all']
        sucess_url = reverse_lazy("blog:all")