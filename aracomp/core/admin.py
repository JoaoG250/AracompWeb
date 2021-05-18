from django.contrib import admin

from core.models import Config


class ConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Config, ConfigAdmin)
