# Generated by Django 2.0.2 on 2018-02-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estagiario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default=1, max_length=1, verbose_name='Sexo'),
            preserve_default=False,
        ),
    ]
