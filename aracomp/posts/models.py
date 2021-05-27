from pathlib import Path
from django.db import models
from django.templatetags.static import static
from django.contrib.staticfiles import finders
from django.utils.crypto import get_random_string
from django.core.exceptions import SuspiciousOperation


class Post(models.Model):
    OPTIONS_POST_TYPE = [
        ('P', 'Palestras'),
        ('H', 'Hackathon'),
        ('M', 'Minicursos')
    ]
    post_type = models.CharField('Tipo de Postagem', max_length=1, choices=OPTIONS_POST_TYPE)
    title = models.CharField('Título', max_length=120)
    description = models.TextField('Descrição', max_length=500)
    content = models.TextField('Conteúdo', max_length=1500)
    image = models.CharField('Path da imagem em static', max_length=200)
    created = models.DateField('Data de Criação', auto_now_add=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def save(self, *args, **kwargs):
        self.image = self.image.replace('/static/', '')
        try:
            if finders.find(self.image):
                self.image = static(self.image)
            else:
                self.image = static('posts/default/post_image.png')
        except SuspiciousOperation:
            self.image = static('posts/default/post_image.png')
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_post_type_display()}: {self.title[:50]}'
