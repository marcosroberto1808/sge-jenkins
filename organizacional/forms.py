from datetime import datetime
from django import forms


def get_my_choices():
    primeiro_ano = 2014
    ano_atual = datetime.now().year

    return tuple(("{}/{}".format(ano, semestre), "{}/{}".format(ano, semestre))
                 for ano in range(ano_atual, primeiro_ano, -1)
                 for semestre in range(1, 3))


class DeclaracaoMatriculaForm(forms.ModelForm):
    periodo_declaracao = forms.ChoiceField(
        label='Periodo da Declaração', choices=get_my_choices())
