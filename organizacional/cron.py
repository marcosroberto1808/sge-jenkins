from .models import Notificacao, Convenio
from datetime import date
from dateutil.relativedelta import relativedelta


three_months_from_today = date.today() + relativedelta(months=+3)

convenios_expirando = Convenio.objects.filter(
    termino_vigencia=three_months_from_today)


def cria_notificacao_convenio_expirando():
    for convenio in convenios_expirando:
        Notificacao.objects.create(
            descricao="Alerta - O convenio com a Instituição {} expira em {}".
            format(convenio.faculdade,
                   convenio.termino_vigencia.strftime('%d/%m/%Y')),
            data_emissao=date.today())
