# Generated by Django 2.2.6 on 2019-10-24 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Festa', '0004_auto_20191024_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluguel',
            options={'verbose_name_plural': 'Alugueis'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-telefone'], 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ['-cep'], 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AlterModelOptions(
            name='itemtema',
            options={'ordering': ['-descricao'], 'verbose_name_plural': 'Itens do Tema'},
        ),
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['-cor_toalha'], 'verbose_name_plural': 'Temas'},
        ),
    ]
