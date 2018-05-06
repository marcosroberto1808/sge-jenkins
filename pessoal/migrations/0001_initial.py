# Generated by Django 2.0.2 on 2018-02-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizacional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Defensor',
                'verbose_name_plural': 'Defensores',
            },
        ),
        migrations.CreateModel(
            name='Estagiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('oab', models.CharField(blank=True, max_length=50, verbose_name='OAB')),
                ('ano', models.CharField(max_length=10, verbose_name='Ano')),
                ('posse', models.DateField(verbose_name='Data da Posse')),
                ('desligamento', models.DateField(blank=True, null=True, verbose_name='Data de Desligamento')),
                ('email_institucional', models.EmailField(max_length=254, verbose_name='E-mail Institucional')),
                ('email_pessoal', models.EmailField(blank=True, max_length=254, verbose_name='E-mail Pessoal')),
                ('nome_mae', models.CharField(max_length=255, verbose_name='Nome da Mãe')),
                ('nome_pai', models.CharField(max_length=255, verbose_name='Nome do Pai')),
                ('rg', models.CharField(max_length=50, verbose_name='RG')),
                ('tipo_estagio', models.CharField(choices=[('Obrigatorio', 'Obrigatorio'), ('Não Obrigatório', 'Não Obrigatório')], max_length=50, verbose_name='Tipo de Estágio')),
                ('turno', models.CharField(choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde')], max_length=50, verbose_name='Turno')),
                ('projeto', models.BooleanField(default=False, verbose_name='Projeto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('defensor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoal.Defensor', verbose_name='Defensor')),
                ('faculdade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizacional.Faculdade', verbose_name='Faculdade')),
                ('lotacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizacional.Lotacao', verbose_name='Lotação')),
                ('situacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizacional.Situacao', verbose_name='Situação')),
                ('vara', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizacional.Vara', verbose_name='Vara')),
            ],
            options={
                'verbose_name': 'Estagiário',
                'verbose_name_plural': 'Estagiários',
            },
        ),
    ]
