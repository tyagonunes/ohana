# Generated by Django 3.2.7 on 2021-10-08 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros_basicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalhador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trabalhador_cidade', to='cadastros_basicos.cidade')),
                ('faixas', models.ManyToManyField(blank=True, related_name='trabalhador_faixas', to='cadastros_basicos.Faixa', verbose_name='Faixas')),
                ('tipo_mediunidade', models.ManyToManyField(blank=True, related_name='trabalhador_tipo_mediunidade', to='cadastros_basicos.TipoMediunidade', verbose_name='Tipos de mediunidade')),
            ],
            options={
                'verbose_name': 'Trabalhador',
                'verbose_name_plural': 'Trabalhadores',
            },
        ),
    ]