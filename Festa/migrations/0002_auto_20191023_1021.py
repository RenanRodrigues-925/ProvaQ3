# Generated by Django 2.2.6 on 2019-10-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Festa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_festa', models.DateField(verbose_name='Data da Festa')),
                ('hora_inicio', models.TimeField(verbose_name='Hora de Inicio')),
                ('hora_termino', models.TimeField(verbose_name='Hora de Termino')),
                ('valor_cobrado', models.CharField(max_length=10, verbose_name='Valor Cobrado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.DateField(max_length=100, verbose_name='Nome')),
                ('telefone', models.TimeField(max_length=10, verbose_name='Telefone')),
                ('Aluguel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Festa.Aluguel')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=6, verbose_name='Numero')),
                ('complemento', models.TextField(max_length=200, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=10, verbose_name='Unidade da Federação')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('Aluguel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festa.Aluguel')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('valor_aluguel', models.CharField(max_length=10, verbose_name='Valor do Aluguel')),
                ('cor_toalha', models.CharField(max_length=50, verbose_name='Cor da Toalha')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='itemtema',
            name='nome_tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festa.Tema'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='tema',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Festa.Tema'),
        ),
    ]
