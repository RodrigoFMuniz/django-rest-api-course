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


    
