from django.db import models

class Tema(models.Model):
    nome = models.CharField('Nome',max_length=100)
    valor_aluguel = models.CharField('Valor do Aluguel',max_length=10)
    cor_toalha = models.CharField('Cor da Toalha',max_length=50)

    class Meta:
        verbose_name_plural = 'Temas'
        ordering = ['-cor_toalha']

    def __str__(self):
        return '{} {} - {}'.format(
            self.data.strftime('%d/%m/%Y'),
            self.hora.strftime('%H:%M'),
        )


class ItemTema(models.Model):
      nome_tema = models.ForeignKey(Tema,on_delete=models.CASCADE)
      descricao = models.TextField('Descrição',max_length=200)

      class Meta:
          verbose_name_plural = 'Itens do Tema'
          ordering = ['-descricao']


class Aluguel(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    data_festa = models.DateField('Data da Festa')
    hora_inicio = models.TimeField('Hora de Inicio')
    hora_termino = models.TimeField('Hora de Termino')
    valor_cobrado = models.CharField('Valor Cobrado',max_length=10)

    class Meta:
        verbose_name_plural = 'Alugueis'

class Endereco(models.Model):
    Aluguel = models.ForeignKey(Aluguel, on_delete=models.CASCADE)
    logradouro = models.CharField('Logradouro',max_length=200)
    numero = models.CharField('Numero',max_length=6)
    complemento = models.TextField('Complemento',max_length=200)
    bairro = models.CharField('Bairro',max_length=200)
    cidade = models.CharField('Cidade',max_length=50)

    UF_CHOICES = [
        ('PI', 'Piaui'),
        ('SP', 'São Paulo'),
        ('CE', 'Ceará'),
        ('MA', 'Maranhão'),
        ('PE', 'Pernambuco')
    ]
    uf = models.CharField('UF',max_length=10,choices=UF_CHOICES,default='PI',)
    cep = models.CharField('CEP',max_length=10)

    class Meta:
        verbose_name_plural = 'Endereços'
        ordering = ['-cep']

class Cliente(models.Model):
    Aluguel_cliente = models.OneToOneField(Aluguel, on_delete=models.CASCADE)
    nome = models.CharField('Nome',max_length=100)
    telefone = models.CharField('Telefone',max_length=12)

    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = ['-telefone']