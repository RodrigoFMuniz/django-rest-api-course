from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
from atracoes.models import Atracao
from .serializers import Atracao_Serializer

class Atracao_Viewset(ModelViewSet):
  queryset = Atracao.objects.all()
  serializer_class = Atracao_Serializer
  filter_backends = [DjangoFilterBackend]
  # filter_backends = [filters.SearchFilter]
  # search_fields = ('name','description')
  filter_fields = ('name','description')
