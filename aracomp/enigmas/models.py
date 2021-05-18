from django.db import models


class RespostaEnigma(models.Model):
    enigma = models.IntegerField('Número do enigma', unique=True)
    resposta = models.CharField('Resposta do enigma', max_length=200)

    def __str__(self):
        return f'Enigma {self.enigma}: {self.resposta}'


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
