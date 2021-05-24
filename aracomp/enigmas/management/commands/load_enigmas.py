import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from enigmas.models import Enigma


class Command(BaseCommand):
    help = 'Importa os enigmas do json'

    def handle(self, *args, **options):
        path = settings.BASE_DIR.joinpath('static', 'assets', 'enigmas.json')
        with open(path) as json_file:
            enigmas = json.load(json_file)
            json_file.close()

        for enigma in enigmas:
            if not Enigma.objects.filter(enigma=enigma['enigma']).exists():
                Enigma.objects.create(**enigma)
                self.stdout.write(self.style.SUCCESS(f'Enigma {enigma["enigma"]} criado'))
