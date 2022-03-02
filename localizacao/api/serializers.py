from rest_framework.serializers import ModelSerializer
from localizacao.models import Localizacao

class Localizacao_Serializer(ModelSerializer):
  class Meta:
    model = Localizacao
    fields = ('id','descricao1','descricao2','cidade','estado','pais','latitude',"longitude")