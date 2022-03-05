from rest_framework.serializers import ModelSerializer
from core.models import Pontos_Turisticos

class Pontos_Turisticos_Serializer(ModelSerializer):
  class Meta:
    model = Pontos_Turisticos
    fields = ('id','name','description','aprovado','foto')