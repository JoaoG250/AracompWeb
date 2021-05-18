from django.views import View
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Config
from enigmas.forms import EnigmaForm, EnigmaVencedorForm
from enigmas.models import VencedorEnigmas, RespostaEnigma

TEMPLATES_ENIGMAS = {
    1: 'enigmas/enigma1.html',
    2: 'enigmas/enigma2.html',
    3: 'enigmas/enigma3.html',
    4: 'enigmas/enigma4.html',
    5: 'enigmas/enigma5.html',
}


class EnigmaView(View):

    def post(self, request, *args, **kwargs):
        # Verificando se a caça ao tesouro já começou
        start = Config.objects.filter(name='enigmas_start').first()
        if not start or not start.active:
            return redirect('home')

        form = EnigmaForm(request.POST)
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            enigma = request.session.get('enigma', 1)

            # Checando se todos os enigmas já foram ultrapassados
            if enigma > 5:
                return redirect('enigmas')

            # Checando resposta
            resposta_enigma = get_object_or_404(RespostaEnigma, enigma=enigma)
            if resposta_enigma.resposta.lower() == resposta.lower():
                enigma += 1
            else:
                messages.warning(request, 'Resposta errada :(, tente novamente.')

            # Atualizando variável do enigma
            request.session['enigma'] = enigma
            return redirect('enigmas')
        context = {
            'form': form,
            'respostas': RespostaEnigma.objects.order_by('enigma')[:enigma - 1],
        }
        return render(request, TEMPLATES_ENIGMAS[enigma], context)

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
            context = {
                'form': EnigmaForm(),
                'vencedor': VencedorEnigmas.objects.first(),
                'respostas': RespostaEnigma.objects.order_by('enigma')[:enigma - 1],
            }
            return render(request, TEMPLATES_ENIGMAS[enigma], context)


class EnigmaFinalizadoView(View):

    def get(self, request, *args, **kwargs):
        enigma = request.session.get('enigma', 1)
        if VencedorEnigmas.objects.count() > 0:
            context = {
                'vencedor': VencedorEnigmas.objects.first(),
                'respostas': RespostaEnigma.objects.order_by('enigma')[:enigma - 1],
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
        else:
            return redirect('enigmas')

    def get(self, request, *args, **kwargs):
        enigma = request.session.get('enigma', 1)
        if VencedorEnigmas.objects.count() == 0 and enigma > 5:
            context = {
                'form': EnigmaVencedorForm(),
                'respostas': RespostaEnigma.objects.order_by('enigma')[:enigma - 1],
            }
            return render(request, 'enigmas/vencedor.html', context)
        else:
            return redirect('enigmas')


class EnigmaReset(View):

    def get(self, request, *args, **kwargs):
        request.session['enigma'] = 1
        return redirect('enigmas')
