from django.contrib import admin

from enigmas.models import VencedorEnigmas, Enigma


class EnigmaAdmin(admin.ModelAdmin):
    pass


class VencedorEnigmasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Enigma, EnigmaAdmin)
admin.site.register(VencedorEnigmas, VencedorEnigmasAdmin)
