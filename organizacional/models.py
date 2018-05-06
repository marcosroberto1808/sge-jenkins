from django.db import models
from .validators import validates_periodo_vinculo, validates_periodo_convenio


class Vara(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vara'
        verbose_name_plural = 'Varas'

    def __str__(self):
        return self.nome


class Lotacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Lotação'
        verbose_name_plural = 'Lotações'

    def __str__(self):
        return self.nome


class Situacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'

    def __str__(self):
        return self.nome


class Faculdade(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Faculdade'
        verbose_name_plural = 'Faculdades'

    def __str__(self):
        return self.nome


class TipoTelefone(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de Telefone'
        verbose_name_plural = 'Tipos de Telefone'

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=50, verbose_name='Número')
    tipe = models.ForeignKey(TipoTelefone, verbose_name='Tipo de Telefone', on_delete=models.PROTECT)
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return '{} - {}'.format(self.tipe.nome, self.numero)


class UnidadeFederativa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    codigo = models.CharField(max_length=2, verbose_name='Código', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federativas'

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    uf = models.ForeignKey(UnidadeFederativa, verbose_name='UF', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return '{} - {}'.format(self.uf.codigo, self.nome)


class Endereco(models.Model):
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiário',
                                   on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, verbose_name='Cidade', on_delete=models.CASCADE)
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    logradouro = models.CharField(max_length=255, verbose_name='Logradouro')
    numero = models.CharField(max_length=15, verbose_name='Número')
    complemento = models.CharField(max_length=255, verbose_name='Complemento', blank=True)
    cep = models.CharField(max_length=100, verbose_name='CEP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return '{}, {} - {}, {} - {}, {}'.format(self.logradouro, self.numero, self.bairro,
                                                 self.cidade.nome, self.cidade.uf.codigo, self.cep)


class Recesso(models.Model):
    inicio = models.DateField(verbose_name='Início')
    termino = models.DateField(verbose_name='Termino')
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiário',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Recesso'
        verbose_name_plural = 'Recessos'

    def __str__(self):
        return 'Período de {} até {}.'.format(self.inicio, self.termino)


class Entregue(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome', unique=True)

    class Meta:
        verbose_name = 'Rel. Entregue'
        verbose_name_plural = 'Rel. Entregues'

    def __str__(self):
        return self.nome


class RelatorioEstagiario(models.Model):
    FREQUENCIA_CHOICES = (
        ('Satisfatória', 'Satisfatória'),
        ('Pendente', 'Pendente'),
        ('Insatisfatória', 'Insatisfatória')
    )
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiário', on_delete=models.PROTECT)
    entregue = models.ForeignKey(Entregue, verbose_name='Rel. Entregue', on_delete=models.PROTECT)
    frequencia = models.CharField(max_length=50, verbose_name='Frequência', choices=FREQUENCIA_CHOICES)

    class Meta:
        verbose_name = 'Relatório de estagiário'
        verbose_name_plural = 'Relatórios de estagiários'


class SuspensaoVinculo(models.Model):
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiario', on_delete=models.CASCADE)
    numero_processo = models.CharField(max_length=100, verbose_name='Nº Processo', unique=True)
    inicio = models.DateField(verbose_name='Início')
    termino = models.DateField(verbose_name='Termino')

    def clean(self, *args, **kwargs):
        validates_periodo_vinculo(self.inicio, self.termino)

    class Meta:
        verbose_name = 'Suspensão de vinculo'
        verbose_name_plural = 'Suspensões de vinculos'


class DeclaracaoMatricula(models.Model):
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiario', on_delete=models.CASCADE)
    data_emissao = models.DateField(verbose_name='Data de Emissão')
    periodo_declaracao = models.CharField(max_length=10, verbose_name='Periodo da Declaração')

    class Meta:
        verbose_name = 'Declaração de Matricula'
        verbose_name_plural = 'Declarações de Matricula'

    def __str__(self):
        return "{} - {}".format(self.estagiario, self.periodo_declaracao)


class Convenio(models.Model):
    faculdade = models.ForeignKey(Faculdade, verbose_name='Faculdade', on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, verbose_name='Cidade', on_delete=models.PROTECT)
    inicio_vigencia = models.DateField(verbose_name='Início da Vigencia')
    termino_vigencia = models.DateField(verbose_name='Termino da Vigencia')

    def clean(self, *args, **kwargs):
        if self._state.adding and hasattr(self, 'faculdade'):
            validates_periodo_convenio(self.faculdade, self.inicio_vigencia,
                                       self.termino_vigencia)

    class Meta:
        verbose_name = 'Convenio Com Instituição de Ensino'
        verbose_name_plural = 'Convenios Com Intituições de Ensino'

    def __str__(self):
        return "{}/{} {} até {}".format(self.faculdade, self.cidade, self.inicio_vigencia, self.termino_vigencia)


class Notificacao(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    data_emissao = models.DateField(verbose_name='Data')

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'

    def __str__(self):
        return self.descricao


class Movimentacao(models.Model):
    estagiario = models.ForeignKey('pessoal.Estagiario', verbose_name='Estagiário', on_delete=models.PROTECT)
    defensor_anterior = models.ForeignKey('pessoal.Defensor', verbose_name='Defensor anterior',
                                          on_delete=models.PROTECT, related_name='defensor_anterior')
    defensor_novo = models.ForeignKey('pessoal.Defensor', verbose_name='Defensor novo', on_delete=models.PROTECT,
                                      related_name='defensor_novo')
    vara_anterior = models.ForeignKey(Vara, verbose_name='Vara anterior', on_delete=models.PROTECT,
                                      related_name='vara_anterior')
    vara_nova = models.ForeignKey(Vara, verbose_name='Vara nova', on_delete=models.PROTECT,
                                  related_name='vara_nova')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')

    class Meta:
        verbose_name = 'Histórico de Movimentação'
        verbose_name_plural = 'Histórico de Movimentações'

    def __str__(self):
        date = '{}/{}/{}'.format(self.created_at.day, self.created_at.month, self.created_at.year)
        return '{} - {}'.format(date, self.estagiario.nome_completo)
