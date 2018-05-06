from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from app.admin import admin_site
from .models import *
from .forms import *
from django.conf import settings


@admin.register(Vara, site=admin_site)
class VaraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Lotacao, site=admin_site)
class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Situacao, site=admin_site)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Faculdade, site=admin_site)
class FaculdadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(TipoTelefone, site=admin_site)
class TipoTelefoneAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(UnidadeFederativa, site=admin_site)
class UnidadeFederativaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome',)
    list_filter = ('codigo', 'nome',)
    ordering = ('codigo',)
    list_per_page = 10


@admin.register(Cidade, site=admin_site)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('uf', 'nome',)
    list_filter = ('uf', 'nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Recesso, site=admin_site)
class RecessoAdmin(admin.ModelAdmin):
    list_display = ('estagiario', 'inicio', 'termino')
    list_filter = ('estagiario', 'inicio', 'termino')
    ordering = ('inicio',)
    list_per_page = 10


@admin.register(Entregue, site=admin_site)
class EntregueAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(RelatorioEstagiario, site=admin_site)
class RelatorioEstagiarioAdmin(admin.ModelAdmin):
    list_display = ('get_estagiario_nome', 'entregue', 'frequencia', 'get_estagiario_oab',
                    'get_estagiario_faculdade', 'get_estagiario_ano', 'get_estagiario_situacao',
                    'get_estagiario_posse')
    list_filter = ('entregue', 'frequencia')
    search_fields = ('estagiario',)
    ordering = ('estagiario',)
    list_per_page = 10

    def get_estagiario_nome(self, obj):
        return obj.estagiario.nome_completo

    get_estagiario_nome.short_description = 'Estagiário'

    def get_estagiario_oab(self, obj):
        return obj.estagiario.oab

    get_estagiario_oab.short_description = 'OAB'

    def get_estagiario_faculdade(self, obj):
        return obj.estagiario.faculdade.nome

    get_estagiario_faculdade.short_description = 'Faculdade'

    def get_estagiario_ano(self, obj):
        return obj.estagiario.ano

    get_estagiario_ano.short_description = 'ANO'

    def get_estagiario_situacao(self, obj):
        return obj.estagiario.situacao

    get_estagiario_situacao.short_description = 'Situação'

    def get_estagiario_posse(self, obj):
        return obj.estagiario.posse.strftime(settings.DATE_FORMAT)

    get_estagiario_posse.short_description = 'Posse'


@admin.register(SuspensaoVinculo, site=admin_site)
class SuspensaoVinculoAdmin(admin.ModelAdmin):
    list_display = ('estagiario', 'numero_processo', 'inicio', 'termino')
    list_filter = ('estagiario', 'numero_processo', 'inicio', 'termino')
    ordering = ('inicio',)
    list_per_page = 10


@admin.register(DeclaracaoMatricula, site=admin_site)
class DeclaracaoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('estagiario', 'data_emissao', 'periodo_declaracao')
    list_filter = ('estagiario', 'data_emissao', 'periodo_declaracao')
    ordering = ('data_emissao',)
    list_per_page = 10
    form = DeclaracaoMatriculaForm


@admin.register(Convenio, site=admin_site)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('faculdade', 'cidade', 'inicio_vigencia', 'termino_vigencia')
    list_filter = ('faculdade', 'cidade', 'inicio_vigencia', 'termino_vigencia')
    ordering = ('inicio_vigencia',)
    list_per_page = 10


@admin.register(Notificacao, site=admin_site)
class NotificacaoAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(Movimentacao, site=admin_site)
class MovimentacaoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    actions = None
    list_display = ('estagiario', 'defensor_anterior', 'vara_anterior', 'defensor_novo', 'vara_nova', 'get_created_at')
    list_filter = (
        ('created_at', DateRangeFilter),
    )
    search_fields = ('estagiario__nome_completo', 'defensor_anterior__nome_completo',
                     'vara_anterior__nome', 'defensor_novo__nome_completo', 'vara_nova__nome')
    list_display_links = None
    list_per_page = 10

    def get_created_at(self, obj):
        return obj.created_at.strftime(settings.DATE_FORMAT)
    get_created_at.short_description = 'Data'


class EnderecoInLine(admin.StackedInline):
    model = Endereco
    extra = 0
    fields = (
        ('cidade', 'bairro', 'logradouro'),
        ('numero', 'cep'),
        ('complemento',)
    )


class TelefoneInLine(admin.TabularInline):
    model = Telefone
    extra = 0


class RecessoInLine(admin.TabularInline):
    model = Recesso
    extra = 0


class SuspensaoVinculoInline(admin.TabularInline):
    model = SuspensaoVinculo
    extra = 0


class MovimentacaoInline(admin.TabularInline):
    model = Movimentacao
    extra = 0
    can_delete = False
    original = ''
    readonly_fields = ('estagiario', 'defensor_anterior', 'vara_anterior', 'defensor_novo', 'vara_nova',
                       'get_created_at')

    def has_add_permission(self, request):
        return False

    def get_created_at(self, obj):
        return obj.created_at.strftime(settings.DATE_FORMAT)
    get_created_at.short_description = 'Data'
