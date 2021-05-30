from django.urls import path

from posts import views
from posts.models import Post

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('cronograma/', views.CronogramaView.as_view(), name='cronograma'),
    path('palestrantes/', views.PalestrantesView.as_view(), name='palestrantes')

]
