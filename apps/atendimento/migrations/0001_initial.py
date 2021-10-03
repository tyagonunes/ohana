# Generated by Django 3.2.7 on 2021-10-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contrib', '0005_terapia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaPretosVelhos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precisa_retorno', models.BooleanField(default=False, verbose_name='Precisa de retorno')),
                ('data', models.DateField(verbose_name='Data')),
                ('recomendacoes', models.TextField(blank=True, null=True, verbose_name='Recomendações')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('consulente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='consultapretosvelhos_consulente', to='contrib.consulente', verbose_name='Consulente')),
                ('entidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='consultapretosvelhos_entidade', to='contrib.entidade', verbose_name='Entidade')),
                ('terapias_recomendadas', models.ManyToManyField(blank=True, related_name='consultapretosvelhos_terapias', to='contrib.Terapia', verbose_name='Terapias recomendadas')),
                ('trabalhadores', models.ManyToManyField(blank=True, related_name='consultapretosvelhos_trabalhadores', to='contrib.Trabalhador', verbose_name='Trabalhadores')),
            ],
            options={
                'verbose_name': 'Consulta Preto Velho',
                'verbose_name_plural': 'Consulta Pretos Velhos',
            },
        ),
    ]
