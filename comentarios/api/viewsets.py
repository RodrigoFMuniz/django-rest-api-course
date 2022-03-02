from rest_framework.viewsets import ModelViewSet
from .serializers import Comentario_Serializer
from comentarios.models import Comentario

class Comentario_Viewset(ModelViewSet):
  queryset = Comentario.objects.all()
  serializer_class = Comentario_Serializer