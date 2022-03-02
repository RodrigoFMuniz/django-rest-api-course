from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao 

class Atracao_Serializer(ModelSerializer):
  class Meta:
    model = Atracao
    fields = ('id','name','description','work_time','min_age')
