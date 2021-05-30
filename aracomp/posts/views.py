from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from posts.models import Post

class PalestrantesView(TemplateView):
    template_name = 'palestrantes.html'

class CronogramaView(TemplateView):
    template_name = 'cronograma.html'

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
