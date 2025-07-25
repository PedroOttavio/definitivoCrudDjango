# Generated by Django 5.1.3 on 2024-12-04 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vitimas', '0004_alter_vitima_abrigo'),
        ('voluntarios', '0002_alter_voluntario_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.TextField(help_text='Descrição do serviço', verbose_name='Descrição')),
                ('prioridade', models.CharField(choices=[('A', 'Alta'), ('M', 'Média'), ('B', 'Baixa')], default='B', help_text='Prioridade do serviço', max_length=20, verbose_name='Prioridade')),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('R', 'Realizado'), ('C', 'Cancelado')], default='A', help_text='Status do serviço', max_length=20, verbose_name='Status')),
                ('vitima', models.ForeignKey(help_text='Vítima atendida', on_delete=django.db.models.deletion.CASCADE, related_name='vitima', to='vitimas.vitima')),
                ('voluntario', models.ForeignKey(help_text='Voluntário que realizou o serviço', on_delete=django.db.models.deletion.CASCADE, related_name='voluntario', to='voluntarios.voluntario')),
            ],
            options={
                'verbose_name': 'Assistencia',
                'verbose_name_plural': 'Assistencias',
            },
        ),
    ]
