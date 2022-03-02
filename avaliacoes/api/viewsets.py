from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import Avaliacao_Serializer

class Avaliacao_Viewset(ModelViewSet):
  queryset = Avaliacao.objects.all()
  serializer_class = Avaliacao_Serializer