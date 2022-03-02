from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class Avaliacao_Serializer(ModelSerializer):
  class Meta:
    model = Avaliacao
    fields = ('id', 'usuario','comentario','nota','data')