from django.contrib import admin
from .models import Categoria, Fornecedor, OpcaoDietetica, Sorvete, comentario

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(OpcaoDietetica)
admin.site.register(Sorvete)
admin.site.register(comentario)
