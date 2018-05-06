from django.contrib.admin import AdminSite as DjAdmSite
from django.contrib.auth.models import User, Group

from auth.admin import UserAdmin
from organizacional.models import Notificacao


class AdminSite(DjAdmSite):
    site_header = 'Sistema de Gerenciamento de Estagiários'

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['notificacoes'] = Notificacao.objects.all().order_by(
            '-data_emissao')[:15]
        return super(AdminSite, self).index(request, extra_context)


admin_site = AdminSite(name='admin')
admin_site.register(Group)
admin_site.register(User, UserAdmin)
