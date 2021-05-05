from pathlib import Path
from django.db import models
from django.utils.crypto import get_random_string


def post_image_path(instance, filename):
    extension = filename.split('.')[-1]
    return Path('post').joinpath('image', f'{get_random_string(10)}.{extension}')


class Post(models.Model):
    OPTIONS_POST_TYPE = [
        ('P', 'Palestra'),
        ('H', 'Hackaton'),
        ('M', 'Minicurso')
    ]
    post_type = models.CharField('Tipo de Postagem', max_length=1, choices=OPTIONS_POST_TYPE)
    title = models.CharField('Título', max_length=120)
    description = models.TextField('Descrição', max_length=500)
    content = models.TextField('Conteúdo', max_length=1500)
    image = models.ImageField('Imagem da Postagem', default='default/post_image.png', upload_to=post_image_path)
    created = models.DateField('Data de Criação', auto_now_add=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return f'{self.get_post_type_display()}: {self.title[:50]}'
