
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
]
```
