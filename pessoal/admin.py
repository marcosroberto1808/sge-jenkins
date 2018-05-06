from django.conf import settings
from django.contrib import admin
from app.admin import admin_site
from rangefilter.filter import DateRangeFilter
from organizacional.admin import TelefoneInLine, EnderecoInLine, RecessoInLine, SuspensaoVinculoInline, \
    MovimentacaoInline
from .models import Estagiario, Defensor


@admin.register(Defensor, site=admin_site)
class DefensorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo',)
    search_fields = ('nome_completo',)
    ordering = ('nome_completo',)
    list_per_page = 10


@admin.register(Estagiario, site=admin_site)
class EstagiarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'defensor', 'vara', 'lotacao',
                    'situacao', 'oab', 'faculdade', 'ano', 'get_posse')
    list_filter = (
        ('posse', DateRangeFilter),
        'tipo_estagio', 'vara', 'lotacao', 'situacao', 'sexo')
    search_fields = ('nome_completo',)
    ordering = ('nome_completo',)
    list_per_page = 10
    inlines = [
        TelefoneInLine,
        EnderecoInLine,
        RecessoInLine,
        SuspensaoVinculoInline,
        MovimentacaoInline
    ]

    def get_posse(self, obj):
        return obj.posse.strftime(settings.DATE_FORMAT)
    get_posse.short_description = 'Posse'
