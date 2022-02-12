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
>> `python manage.py startapp core`

    