from django.urls import path

from posts import views
from posts.models import Post

urlpatterns = [
    path('', views.PostsView.as_view(), name='home')
]
