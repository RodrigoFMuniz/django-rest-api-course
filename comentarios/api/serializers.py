from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class Comentarios_Serializer(ModelSerializer):
  class Meta:
    model = Comentario
    fields = ('id','usuario','comentarios','data_comentario','aprovado')