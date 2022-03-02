from rest_framework.viewsets import ModelViewSet
from .serializers import Comentarios_Serializer
from comentarios.models import Comentario

class Comentarios_Viewset(ModelViewSet):
  queryset = Comentario.objects.all()
  serializer_class = Comentarios_Serializer