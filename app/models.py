from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# Modelo personalizado de usuário
class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        USUARIO = "usuario", _("Usuário")
        PROFISSIONAL = "profissional", _("Profissional")
        ADMINISTRADOR = "administrador", _("Administrador")

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.USUARIO,
    )
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to="fotos_perfil/", null=True, blank=True)


class RegistroHumor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="registros_humor")
    data = models.DateField(auto_now_add=True)
    humor = models.IntegerField()  # Escala de 1 a 10
    eventos = models.TextField(null=True, blank=True)
    anotacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Registro de Humor de {self.usuario.email} em {self.data}"


class Recomendacao(models.Model):
    registro_humor = models.ForeignKey(RegistroHumor, on_delete=models.CASCADE, related_name="recomendacoes")
    descricao = models.TextField()

    def __str__(self):
        return f"Recomendação para Registro de Humor {self.registro_humor.id}"


class Relatorio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="relatorios_enviados")
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="relatorios_recebidos")
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Relatório compartilhado por {self.usuario.email} para {self.profissional.email}"


class Postagem(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    categorias = models.CharField(max_length=255, null=True, blank=True)
    links = models.URLField(max_length=200, null=True, blank=True)
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="postagens")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
