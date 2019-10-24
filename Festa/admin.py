from django.contrib import admin
from .models import *
from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome','valor_aluguel','cor_toalha')

admin.site.register(Tema,TemaAdmin)

class ItemTemaAdmin(admin.ModelAdmin):
    list_display = ('nome_tema','descricao')

admin.site.register(ItemTema,ItemTemaAdmin)

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('tema','data_festa','hora_inicio','hora_termino','valor_cobrado')

admin.site.register(Aluguel,AluguelAdmin)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('Aluguel','logradouro','numero','complemento','bairro','cidade','uf','cep')

admin.site.register(Endereco,EnderecoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Aluguel_cliente','nome','telefone')

admin.site.register(Cliente,ClienteAdmin)
admin.site.site_header = 'Painel de Controle de Festas'
admin.site.index_title = 'Festas'
admin.site.site_title = 'Controle de Festas'
