from django.db import models

# Create your models here.
class Atracao(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  work_time = models.TextField()
  min_age = models.IntegerField()
  foto = models.ImageField(upload_to='atracoes',null=True,blank=True)

  def __str__(self):
    return self.name