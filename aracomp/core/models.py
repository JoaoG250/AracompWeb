from django.db import models


class Config(models.Model):
    name = models.SlugField('Nome da configuração', unique=True)
    active = models.BooleanField('Status da configuração', default=False)

    def __str__(self):
        return f'{self.name}: {self.active}'