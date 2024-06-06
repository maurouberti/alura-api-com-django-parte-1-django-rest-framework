
![Static Badge](https://img.shields.io/badge/Alura-%230b182c)
![Static Badge](https://img.shields.io/badge/Django-4.2.13-%23092E20?logoColor=ffffff)


# 1 - Instalando o Django Rest API

O Django pode ser instalado através do comando:

```
pip install Django==4.2.13
```

Criar um ambiente virtual com o seguinte comando:

```
virtualenv venv
```

Ativar seu ambiente virtual com o seguinte comando:

```
source venv/bin/activate
```

Instalar o Django nesse ambiente virtualizado:

```
pip install django
```

Criar um **projeto** chamado **setup** utilizando o Django admin:

```
django-admin startproject setup .
```

Alterar o arquivo **setup/settings.py** o idioma e o horário:

```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

Criar app escola:

```
python manage.py startapp escola
```

Instalar dois pacotes, o **Django Rest Framework** e o **Markdown**:

```
pip install djangorestframework
pip install markdown
```

Adicionar no arquivo **setup/settings.py** o Django Rest Framework como um APP instalado:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'escola',
]
```

# 2 - Modelos, Admin e Serializers

Alterar arquivo **escola/models.py** e depois criar as **migrations** com o comando:

```
python manage.py makemigrations
```

Executar as **migrations**:

```
python manage.py migrate
```

Configurar a área **admin**.  
Alterar arquivo **escola/admin.py**

Criar usuário para área **admin**

```
python manage.py createsuperuser
```

Criar arquivo **escola/serializer.py**

# 3 - Viewset, Urls e requisições GET e POST

Alterar arquivo **escola/views.py**  
Alterar arquivo **setup/urls.py**  

```
...
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    ...
    path('', include(router.urls)),
]
```

# 4 - Atualizando e deletando recursos

Alterar arquivo **escola/models.py** e adicionar **model matricula** e depois criar as **migrations** com o comando:

```
python manage.py makemigrations
```

Executar as **migrations**:

```
python manage.py migrate
```

Configurar a área **admin**.  
Alterar arquivo **escola/admin.py**

Alterar arquivo **escola/serializer.py**  
Alterar arquivo **escola/views.py**  
Alterar arquivo **setup/urls.py**  
