from django.contrib import admin
from produto.models import Produto

class ProdutoADM(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Produto, ProdutoADM)