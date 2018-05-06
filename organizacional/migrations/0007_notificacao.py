# Generated by Django 2.0.2 on 2018-03-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizacional', '0006_convenio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('data_emissao', models.DateField(verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
    ]
