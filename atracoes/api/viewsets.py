from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import Atracao_Serializer

class Atracoes_Viewse(ModelViewSet):
  queryset = Atracao.objects.all()
  serializer_class = Atracao_Serializer
