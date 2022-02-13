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



