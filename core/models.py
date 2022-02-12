from django.db import models

# Create your models here.
class Pontos_Turisticos(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  aprovado = models.BooleanField(default=False)

  def __str__(self):
    return self.name
