from django.db import models
from organizacional.models import Vara, Lotacao, Situacao, Faculdade, Endereco


class Defensor(models.Model):
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Defensor'
        verbose_name_plural = 'Defensores'

    def __str__(self):
        return self.nome_completo


class Estagiario(models.Model):
    TIPO_ESTAGIO_CHOICES = (
        ('Obrigatorio', 'Obrigatorio'),
        ('Não Obrigatório', 'Não Obrigatório'),
    )
    TURNO_CHOICES = (
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde')
    )
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    oab = models.CharField(max_length=50, blank=True, verbose_name='OAB')
    ano = models.CharField(max_length=10, verbose_name='Ano')
    posse = models.DateField(verbose_name='Data da Posse')
    desligamento = models.DateField(verbose_name='Data de Desligamento', null=True, blank=True)
    email_institucional = models.EmailField(verbose_name='E-mail Institucional')
    email_pessoal = models.EmailField(verbose_name='E-mail Pessoal', blank=True)
    nome_mae = models.CharField(max_length=255, verbose_name='Nome da Mãe')
    nome_pai = models.CharField(max_length=255, verbose_name='Nome do Pai')
    rg = models.CharField(max_length=50, verbose_name='RG')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=SEXO_CHOICES)
    tipo_estagio = models.CharField(max_length=50, choices=TIPO_ESTAGIO_CHOICES,
                                    verbose_name='Tipo de Estágio')
    turno = models.CharField(max_length=50, choices=TURNO_CHOICES, verbose_name='Turno')
    projeto = models.BooleanField(default=False, verbose_name='Projeto')
    defensor = models.ForeignKey(Defensor, verbose_name='Defensor', on_delete=models.PROTECT)
    vara = models.ForeignKey(Vara, verbose_name='Vara', on_delete=models.PROTECT)
    lotacao = models.ForeignKey(Lotacao, verbose_name='Lotação', on_delete=models.PROTECT)
    situacao = models.ForeignKey(Situacao, verbose_name='Situação', on_delete=models.PROTECT)
    faculdade = models.ForeignKey(Faculdade, verbose_name='Faculdade', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Estagiário'
        verbose_name_plural = 'Estagiários'

    def __str__(self):
        return self.nome_completo

    def save(self, *args, **kwargs):
        from organizacional.models import Movimentacao
        if self.pk > 0:
            old_estagiario = Estagiario.objects.get(pk=self.pk)
            if old_estagiario.defensor != self.defensor or old_estagiario.vara != self.vara:
                movimentacao = Movimentacao()
                movimentacao.estagiario = old_estagiario
                movimentacao.defensor_anterior = old_estagiario.defensor
                movimentacao.defensor_novo = self.defensor
                movimentacao.vara_anterior = old_estagiario.vara
                movimentacao.vara_nova = self.vara
                movimentacao.save()
        super().save(*args, **kwargs)
