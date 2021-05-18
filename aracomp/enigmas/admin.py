from django.contrib import admin

from enigmas.models import VencedorEnigmas, RespostaEnigma


class RespostaEnigmaAdmin(admin.ModelAdmin):
    pass


class VencedorEnigmasAdmin(admin.ModelAdmin):
    pass


admin.site.register(RespostaEnigma, RespostaEnigmaAdmin)
admin.site.register(VencedorEnigmas, VencedorEnigmasAdmin)
