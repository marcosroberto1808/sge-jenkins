from django.core.exceptions import ValidationError
from dateutil import relativedelta


def validates_periodo_vinculo(inicio, termino):
    if relativedelta.relativedelta(termino, inicio).months > 6:
        raise ValidationError(
            ('O prazo limite de uma suspensão de vínculo é de até 6 meses'), )


def validates_periodo_convenio(faculdade, inicio, termino):
    from .models import Convenio
    convenios = Convenio.objects.filter(faculdade=faculdade)

    convenios = convenios.filter(inicio_vigencia__range=(
        inicio, termino
    )) | convenios.filter(termino_vigencia__range=(inicio, termino))

    if convenios:
        raise ValidationError((
            'Não é permitido criar convenios com periodos concomitantes para uma mesma instituição'
        ), )
