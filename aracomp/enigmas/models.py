from django.db import models
from django.templatetags.static import static


class Enigma(models.Model):
    enigma = models.PositiveIntegerField('Número do enigma', unique=True)
    pergunta = models.CharField('Pergunta', max_length=100)
    pagina = models.CharField('Nome da página', max_length=100)
    resposta = models.CharField('Resposta do enigma', max_length=100)

    def __str__(self):
        return f'Enigma {self.enigma}: {self.resposta}'

    def get_img_uri(self):
        return static(f'assets/img/enigma{self.enigma}.png')

    def checar_resposta(self, resposta):
        return self.resposta.lower() == resposta.lower()


class VencedorEnigmas(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')

    def save(self, *args, **kwargs):
        if VencedorEnigmas.objects.count() == 0:
            super(VencedorEnigmas, self).save(*args, **kwargs)
        else:
            raise Exception

    def __str__(self):
        return f'{self.nome} | {self.email}'
