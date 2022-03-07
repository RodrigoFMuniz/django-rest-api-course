from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import Localizacao_Serializer
from localizacao.models import Localizacao

class Localizacao_Viewset(ModelViewSet):
  queryset = Localizacao.objects.all()
  serializer_class = Localizacao_Serializer


