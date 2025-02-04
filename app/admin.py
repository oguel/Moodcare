from django.contrib import admin
from .models import *

class RecomendacaoInline(admin.TabularInline):
    model = Recomendacao
    extra = 1


class RegistroHumorInline(admin.TabularInline):
    model = RegistroHumor
    extra = 1


class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 1
    fk_name = "usuario"


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "tipo_usuario", "data_nascimento")
    list_filter = ("tipo_usuario",)
    inlines = [RegistroHumorInline, RelatorioInline]


@admin.register(RegistroHumor)
class RegistroHumorAdmin(admin.ModelAdmin):
    list_display = ("usuario", "data", "humor")
    list_filter = ("data", "humor")
    inlines = [RecomendacaoInline]


@admin.register(Recomendacao)
class RecomendacaoAdmin(admin.ModelAdmin):
    list_display = ("registro_humor", "descricao")


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "profissional", "criado_em")
    list_filter = ("criado_em",)


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criado_por", "criado_em")
    list_filter = ("criado_em",)

    
