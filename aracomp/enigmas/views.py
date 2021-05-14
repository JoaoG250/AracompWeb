from django.views import View
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Config
from enigmas.models import VencedorEnigmas, Enigma
from enigmas.forms import RespostaEnigmaForm, EnigmaVencedorForm


def get_respostas(enigma):
    respostas = list(Enigma.objects.order_by('enigma')[:enigma - 1].values_list('resposta', flat=True))
    for i in range(len(respostas) + 1, 6):
        respostas.append('????')
    return respostas


class EnigmaView(View):

    def post(self, request, *args, **kwargs):
        # Verificando se a caça ao tesouro já começou
        start = Config.objects.filter(name='enigmas_start').first()
        if not start or not start.active:
            return redirect('home')

        form = RespostaEnigmaForm(request.POST)
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            enigma = request.session.get('enigma', 1)

            # Checando se todos os enigmas já foram ultrapassados
            if enigma > 5:
                return redirect('enigmas')

            # Checando resposta
            enigma_obj = get_object_or_404(Enigma, enigma=enigma)
            if enigma_obj.checar_resposta(resposta):
                enigma += 1
            else:
                messages.warning(request, 'Resposta errada :(, tente novamente.')

            # Atualizando variável do enigma
            request.session['enigma'] = enigma
            return redirect('enigmas')

        context = {
            'form': form,
            'respostas': get_respostas(enigma),
        }
        return render(request, 'enigmas/enigma.html', context)

    def get(self, request, *args, **kwargs):
        # Verificando se a caça ao tesouro já começou
        start = Config.objects.filter(name='enigmas_start').first()
        if not start or not start.active:
            return redirect('home')

        enigma = request.session.get('enigma', 1)
        if enigma > 5:
            if VencedorEnigmas.objects.count() > 0:
                return redirect('enigmas-finalizado')
            return redirect('enigmas-vencedor')
        else:
            enigma_obj = get_object_or_404(Enigma, enigma=enigma)
            context = {
                'form': RespostaEnigmaForm(),
                'vencedor': VencedorEnigmas.objects.first(),
                'enigma': enigma_obj,
                'respostas': get_respostas(enigma),
            }
            return render(request, 'enigmas/enigma.html', context)


class EnigmaFinalizadoView(View):

    def get(self, request, *args, **kwargs):
        enigma = request.session.get('enigma', 1)
        if VencedorEnigmas.objects.count() > 0 and enigma > 5:
            context = {
                'vencedor': VencedorEnigmas.objects.first(),
                'respostas': get_respostas(enigma),
            }
            return render(request, 'enigmas/finalizado.html', context)
        else:
            return redirect('enigmas')


class EnigmaVencedorView(View):

    def post(self, request, *args, **kwargs):
        enigma = request.session.get('enigma', 1)
        if VencedorEnigmas.objects.count() == 0 and enigma > 5:
            form = EnigmaVencedorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Você é o ganhador da caça ao tesouro. Parabêns!!')
                return redirect('enigmas-finalizado')
            context = {
                'form': form,
                'respostas': get_respostas(enigma),
            }
            return render(request, 'enigmas/vencedor.html', context)
        else:
            return redirect('enigmas')

    def get(self, request, *args, **kwargs):
        enigma = request.session.get('enigma', 1)
        if VencedorEnigmas.objects.count() == 0 and enigma > 5:
            context = {
                'form': EnigmaVencedorForm(),
                'respostas': get_respostas(enigma),
            }
            return render(request, 'enigmas/vencedor.html', context)
        else:
            return redirect('enigmas')


class EnigmaReset(View):

    def get(self, request, *args, **kwargs):
        request.session['enigma'] = 1
        return redirect('enigmas')
