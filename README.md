# Django Rest API Course
## Init Steps  / Launching
### -> Set Virtual Environment
> - `python -m venv venv`
> - `.\venv\Scripts\activate.bat` (***for windows***)
> - `source venv/bin/activate` (***for Linux / mac***)
### -> Create Requirements.txt
> - Create Requirements.txt
> - Insert Django version into It ex. django==3.2.5
> - Execute ->  `python -m pip install -r Requirements.txt`

### -> Starting a Django project 
> - Browse to project folder (*same level of venv folder*)
> - Execute command line ->  `python -m django startproject project_name .` (to the project root directory) or nothing to create another folder at second level. 
>- First option recommended.
### -> Install djangorestframework
> - Execute ->  `python -m pip install djangorestframework`
> - (or)->  `pip install djangorestframework`
> - (or) register djangorestframework into Requirements.txt and execute->  `python -m pip install -r Requirements.txt`
### -> Create superuser
> - Create superuser by using the following command
>> `python manage.py createsuperuser`
> - Insert User name, email and password
### -> Execute migrate
>>`python manage.py migrate`
### -> Start app core
> - Declare into INSTALLED_APPS in settings.py
>> `python manage.py startapp core`
### -> Start Modeling the models(tables) of project
>from django.db import models

### -> Create your models here.
>       class Pontos_Turisticos(models.Model):
>          name = models.CharField(max_length=150)
>          description = models.TextField()
>          aprovado = models.BooleanField(default=False)
>
>          def __str__(self):
>            return self.name

### -> Allow access to the Dashboard to your Models as admin
>         from django.contrib import admin
>         from .models import Pontos_Turisticos
>         admin.site.register(Pontos_Turisticos)

### -> Create a sub-folder called api into you app, at same level of migrations
> - Transform It creating a file called ***\_\_init\_\_.py***
> - Create the file ***serializers.py***
> - Create the file ***viewsets.py***

### -> Create atracoes app
> 1. Use command:
>> `python manage.py startapp atracoes`
> 2. Register into INSTALLED_APPS in settings.py 
> 3. Define your table by creating a model class
> 4. Register the class into admin.py using the command line:
>> `admin.site.register(Atracao)`
> 5. Make migration using the command line:
>> `python manage.py makemigrations`
> 6. Create a table using migrate command:
>> `python manage.py migrate`

### -> Create avaliacoes app
> 1. Use command:
>> `python manage.py startapp avaliacoes`
> 2. Register into INSTALLED_APPS in settings.py 
> 3. Define your table by creating a model class
> 4. Register the class into admin.py using the command line:
>> `admin.site.register(Avaliacao)`
> 5. Make migration using the command line:
>> `python manage.py makemigrations`
> 6. Create a table using migrate command:
>> `python manage.py migrate`
### -> Repeat step *Create a sub-folder called api into you app, at same level of migrations*

### -> Create comentarios app
> 1. Use command:
>> `python manage.py startapp comentarios`
> 2. Register into INSTALLED_APPS in settings.py 
> 3. Define your table by creating a model class
> 4. Register the class into admin.py using the command line:
>> `admin.site.register(Comentario)`
> 5. Make migration using the command line:
>> `python manage.py makemigrations`
> 6. Create a table using migrate command:
>> `python manage.py migrate`
### -> Repeat step *Create a sub-folder called api into you app, at same level of migrations*

### -> Create localizacao app
> 1. Use command:
>> `python manage.py startapp localizacao`
> 2. Register into INSTALLED_APPS in settings.py 
> 3. Define your table by creating a model class
> 4. Register the class into admin.py using the command line:
>> `admin.site.register(Localizacao)`
> 5. Make migration using the command line:
>> `python manage.py makemigrations`
> 6. Create a table using migrate command:
>> `python manage.py migrate`
### -> Repeat step *Create a sub-folder called api into you app, at same level of migrations*



### Relationship between tables
#### Creating a relationship Many to Many between Pontos Turisticos and atracoes
        from django.db import models
        from atracoes.models import Atracao

        class Pontos_Turisticos(models.Model):
          name = models.CharField(max_length=150)
          description = models.TextField()
          aprovado = models.BooleanField(default=False)
          atracoes = models.ManyToManyField(Atracao)

          def __str__(self):
            return self.name



#### Creating a relationship Many to Many between Pontos Turisticos and comentarios

        from django.db import models
        from  django.contrib.auth.models import User

        from pontos_turisticos.settings import DEFAULT_AUTO_FIELD

        class Comentario(models.Model):
          usuario = models.ForeignKey(User,on_delete= models.CASCADE)
          comentarios = models.TextField()
          data_comentario = models.DateTimeField(auto_now_add=True)
          aprovado = models.BooleanField(default=True)

          def __str__(self):
            return self.usuario.username


#### Creating a relationship Many to Many between Pontos Turisticos and avaliacoes
            
        from django.db import models
        from atracoes.models import Atracao
        from comentarios.models import Comentario
        from avaliacoes.models import Avaliacao

        class Pontos_Turisticos(models.Model):
          name = models.CharField(max_length=150)
          description = models.TextField()
          aprovado = models.BooleanField(default=False)
          atracoes = models.ManyToManyField(Atracao)
          comentarios = models.ManyToManyField(Comentario)
          avaliacoes = models.ManyToManyField(Avaliacao)

          def __str__(self):
            return self.name

#### Creating a relationship 1:1 between Pontos Turisticos and localizacao
        from django.db import models
        from atracoes.models import Atracao
        from comentarios.models import Comentario
        from avaliacoes.models import Avaliacao
        from localizacao.models import Localizacao

        class Pontos_Turisticos(models.Model):
          name = models.CharField(max_length=150)
          description = models.TextField()
          aprovado = models.BooleanField(default=False)
          atracoes = models.ManyToManyField(Atracao)
          comentarios = models.ManyToManyField(Comentario)
          avaliacoes = models.ManyToManyField(Avaliacao)
          localizacao = models.ForeignKey(Localizacao,on_delete=models.CASCADE)

          def __str__(self):
            return self.name

## Building our API 

### Pontos_Turisticos endpoint

#### Creating a Viewsets class into viewsets file 

        from rest_framework.viewsets import ModelViewSet
        from core.models import Pontos_Turisticos
        from .serializers import Pontos_Turisticos_Serializer

        class Pontos_Turisticos_ViewSet(ModelViewSet):
          queryset = Pontos_Turisticos.objects.all()
          serializer_class = Pontos_Turisticos_Serializer

#### Creating a Serializers Class into serializers file

        from rest_framework.serializers import ModelSerializer
        from core.models import Pontos_Turisticos

        class Pontos_Turisticos_Serializer(ModelSerializer):
          class Meta:
            model = Pontos_Turisticos
            fields = ('id','description','aprovado')


### atracoes endpoint

#### Registering atracoes endpoint into urls.py


        from atracoes.api.viewsets import Atracoes_Viewset

        router.register(r'atracoes', Atracoes_Viewset)

#### Creating a atracoes.viewsets code

        from rest_framework.viewsets import ModelViewSet
        from atracoes.models import Atracao
        from .serializers import Atracao_Serializer

        class Atracoes_Viewset(ModelViewSet):
          queryset = Atracao.objects.all()
          serializer_class = Atracao_Serializer

#### Creating a atracoes.serializers code

        from rest_framework.serializers import ModelSerializer
        from atracoes.models import Atracao 

        class Atracao_Serializer(ModelSerializer):
          class Meta:
            model = Atracao
            fields = ('id','name','description','work_time','min_age')

### Localização endpoint

#### Registering localizacao endpoint into urls.py

        from localizacao.api.viewsets import Localizacao_Viewset

        router.register(r'localizacao', Localizacao_Viewset)

#### Creating a localizacao.viewsets code

        from rest_framework.viewsets import ModelViewSet
        from localizacao.models import Localizacao
        from .serializers import Localizacao_Serializer

        class Localizacao_Viewset(ModelViewSet):
          queryset = Localizacao.objects.all()
          serializer_class = Localizacao_Serializer

#### Creating a localizacao.serializers code

        from rest_framework.serializers import ModelSerializer
        from localizacao.models import Localizacao 

        class Localizacao_Serializer(ModelSerializer):
          class Meta:
            model = Localizacao
            fields = ('id','descricao1','descricao2','cidade','estado','pais','latitude',"longitude")

### Comentários endpoint

#### Registering comentarios endpoint into urls.py

        from comentarios.api.viewsets import Comentarios_Viewset

        router.register(r'comentarios', Comentarios_Viewset)

#### Creating a comentarios.viewsets code

        from rest_framework.viewsets import ModelViewSet
        from .serializers import Comentarios_Serializer
        from comentarios.models import Comentario

        class Comentarios_Viewset(ModelViewSet):
          queryset = Comentario.objects.all()
          serializer_class = Comentarios_Serializer

#### Creating a comentarios.serializers code

        from rest_framework.serializers import ModelSerializer
        from comentarios.models import Comentario

        class Comentarios_Serializer(ModelSerializer):
          class Meta:
            model = Comentario
            fields = ('id','usuario','comentarios','data_comentario','aprovado')


### Avaliacao endpoint

#### Registering avaliacoes endpoint into urls.py

        from avaliacoes.api.viewsets import Avaliacao_Viewset

        router.register(r'avaliacoes', Avaliacao_Viewset)

#### Creating a avaliacoes.viewsets code

        from rest_framework.viewsets import ModelViewSet
        from avaliacoes.models import Avaliacao
        from .serializers import Avaliacao_Serializer

        class Avaliacao_Viewset(ModelViewSet):
          queryset = Avaliacao.objects.all()
          serializer_class = Avaliacao_Serializer

#### Creating a avaliacoes.serializers code

        from rest_framework.serializers import ModelSerializer
        from avaliacoes.models import Avaliacao

        class Avaliacao_Serializer(ModelSerializer):
          class Meta:
            model = Avaliacao
            fields = ('id', 'usuario','comentario','nota','data')

## Advanced query methods

### get_queryset(self)  ====    Get

* urls.py

        router.register(r'pontos_turisticos', Pontos_Turisticos_ViewSet,basename=Pontos_Turisticos)

* pontos_turisticos.api.viewsets

          def get_queryset(self):
              return Pontos_Turisticos.objects.all()


### list(self)   =====   Get

* Override get_queryset method

          def list(self, request, *args, **kwargs):
              return Response({'teste':123})

### retrieve(self)   ====   Get

        def retrieve(self, request, *args, **kwargs):
            params = kwargs
            print(params)
            param_list = params["pk"].split('-')
            print(param_list)
            p_turismo= Pontos_Turisticos.objects.filter(name = param_list[0],description=param_list[1])
            serializer = Pontos_Turisticos_Serializer(p_turismo, many=True)
            return Response(serializer.data)

### create(self)   =====  Post

        def create(self, request, *args, **kwargs):
          validated_data = request.data
          if validated_data["name"]=="Praia de Copacabana":
            new_ponto_turistico = Pontos_Turisticos.objects.create(
            name=validated_data["name"],description=validated_data["description"],aprovado=validated_data["aprovado"]
            )
            new_ponto_turistico.save()
            serializer = Pontos_Turisticos_Serializer(new_ponto_turistico)
            return Response(serializer.data)
          return Response({"erro":"name inválido"})

### destroy(self)   ===== Delete

        def destroy(self, request, *args, **kwargs):
            params=kwargs
            obj = Pontos_Turisticos.objects.filter(id = params["pk"])
            print(params)
            # print(obj)
            if obj:
              obj.delete()
              return Response({"Resposta":"Destruído com sucesso"})
            return Response({"Resposta":"Objeto não encontrado"})
                
### update(self)  ==== Put
        def update(self, request, *args, **kwargs):
            requ = request.data
            print(requ)
            kw = kwargs
            print(kw)
            search = Pontos_Turisticos.objects.filter(id = kw['pk'])
            print(search)

            if search:
              data_updated = Pontos_Turisticos.objects.update(name=requ["name"],description=requ["description"])
              search.save()
              serializer = Pontos_Turisticos_Serializer(data_updated)
              return Response(serializer.data)
            return Response({"erro":"Objeto inexistente"})

### partial_update(self)  ====   Patch
          
          def partial_update(self, request, *args, **kwargs):
              pass

### custom_action(self)  ====   All verbs

          from rest_framework.decorators import action

          @action(methods=['get','post'], detail=True)
          def metodo_personalizado(self, request, ph=None):
            pass

## Working with images

* install Pillow package

        python -m pip install Pillow

* models.py

        foto = models.ImageField(upload_to='pontos_turisticos',null=True,blank=True)

* urls.py

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',include(router.urls))
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## Using query strings as search tool

        def get_queryset(self):
          id= self.request.query_params.get('id', None)
          name= self.request.query_params.get('name',None)
          description= self.request.query_params.get('description', None)
          queryset = Pontos_Turisticos.objects.all()
          if id:
            queryset = queryset.filter(pk=id)
          if name:
            queryset = queryset.filter(name__iexact=name)
          if description:
            queryset = queryset.filter(description=description)
          
          return queryset


## Using lookup_field 

* lookup_field must be used everytime you want to change the search key from a default(id) to another one. It must have a primary key behavior because that feature doesn't support multiple returns.

        lookup_field = 'name'