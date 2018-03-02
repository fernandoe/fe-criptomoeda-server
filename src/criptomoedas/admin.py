from django.contrib import admin

from .models import Moeda


@admin.register(Moeda)
class MoedaModelAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'codigo' ]
    list_display = ['get_uuid', 'nome', 'codigo']
