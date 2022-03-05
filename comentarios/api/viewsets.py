from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers import Comentario_Serializer
from comentarios.models import Comentario

class Comentario_Viewset(ModelViewSet):
  queryset = Comentario.objects.all()
  serializer_class = Comentario_Serializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['comentarios']