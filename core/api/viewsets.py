from msilib.schema import Error
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Pontos_Turisticos
from .serializers import Pontos_Turisticos_Serializer

class Pontos_Turisticos_ViewSet(ModelViewSet):
  # queryset = Pontos_Turisticos.objects.all()
  serializer_class = Pontos_Turisticos_Serializer

  def get_queryset(self):
      return Pontos_Turisticos.objects.all()

  def list(self, request, *args, **kwargs):
      return super(Pontos_Turisticos_ViewSet, self).list(request, *args, **kwargs)
  # def retrieve(self, request, *args, **kwargs):
  #     params = kwargs
  #     user_logged = request.user
  #     print(user_logged)
  #     param_list = params["pk"].split('-')
  #     print(param_list)
  #     p_turismo= Pontos_Turisticos.objects.filter(name = param_list[0],description=param_list[1])
  #     serializer = Pontos_Turisticos_Serializer(p_turismo, many=True)
  #     return Response(serializer.data)

  # def create(self, request, *args, **kwargs):
  #   validated_data = request.data
  #   if validated_data["name"]=="Praia de Copacabana":
  #     new_ponto_turistico = Pontos_Turisticos.objects.create(
  #     name=validated_data["name"],description=validated_data["description"],aprovado=validated_data["aprovado"]
  #     )
  #     new_ponto_turistico.save()
  #     serializer = Pontos_Turisticos_Serializer(new_ponto_turistico)
  #     return Response(serializer.data)
  #   return Response({"erro":"name inválido"})
    
  def create(self, request, *args, **kwargs):
      return super(Pontos_Turisticos_ViewSet, self).create(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
      return super(Pontos_Turisticos_ViewSet, self).destroy(request, *args, **kwargs)

  # def destroy(self, request, *args, **kwargs):
  #   params=kwargs
  #   obj = Pontos_Turisticos.objects.filter(id = params["pk"])
  #   print(params)
  #   # print(obj)
  #   if obj:
  #     obj.delete()
  #     return Response({"Resposta":"Destruído com sucesso"})
  #   return Response({"Resposta":"Objeto não encontrado"})

  # def update(self, request, *args, **kwargs):
  #     requ = request.data
  #     print(requ)
  #     kw = kwargs
  #     print(kw)
  #     search = Pontos_Turisticos.objects.filter(id = kw['pk'])
  #     print(search)

  #     if search:
  #       data_updated = Pontos_Turisticos.objects.update(name=requ["name"],description=requ["description"])
  #       search.save()
  #       serializer = Pontos_Turisticos_Serializer(data_updated)
  #       return Response(serializer.data)
  #     return Response({"erro":"Objeto inexistente"})
  
  def update(self, request, *args, **kwargs):
      return super(Pontos_Turisticos_ViewSet,self).update(self, request, *args, **kwargs)
  
  def partial_update(self, request, *args, **kwargs):
      return super(Pontos_Turisticos_ViewSet, self).partial_update(self, request, *args, **kwargs)

  # @action(methods=['get','post'], detail=True)
  # def metodo_personalizado(self, request, ph=None):
  #   pass