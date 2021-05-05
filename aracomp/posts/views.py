from django.shortcuts import render
from django.views.generic.list import ListView

from posts.models import Post


class PostsView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        return context
