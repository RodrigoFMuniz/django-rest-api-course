from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao

# Create your models here.
class Pontos_Turisticos(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  aprovado = models.BooleanField(default=False)
  atracoes = models.ManyToManyField(Atracao)
  comentarios = models.ManyToManyField(Comentario)
  avaliacoes = models.ManyToManyField(Avaliacao)
  localizacao = models.ForeignKey(Localizacao,on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return self.name
