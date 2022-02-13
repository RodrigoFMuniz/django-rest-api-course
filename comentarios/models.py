from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Comentario(models.Model):
  usuario = models.ForeignKey(User,on_delete= models.CASCADE)
  comentarios = models.TextField()
  data_comentario = models.DateTimeField(auto_now_add=True)
  aprovado = models.BooleanField(default=True)

  def __str__(self):
    return self.usuario.username

