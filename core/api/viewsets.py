from rest_framework.viewsets import ModelViewSet
from core.models import Pontos_Turisticos
from .serializers import Pontos_Turisticos_Serializer

class Pontos_Turisticos_ViewSet(ModelViewSet):
  queryset = Pontos_Turisticos.objects.all()
  serializer_class = Pontos_Turisticos_Serializer