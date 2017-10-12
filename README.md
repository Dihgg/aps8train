# APS 8
> Programa Desenvolvido para o 8º semestre do curso de Ciência da computação UNIP
## Pré-requisistos
- Python
  - virtualenv
- Git
- mySql

## Rodar localmente
> As informações de conexão do banco de dados estão em `aps8/settings.py`
> Certifique-se de que estão certas antes de continuar
 
Criar um ambiente virtual utilizando o `virtualenv`
```sh
$   virtualenv env
```
Iniciar o anbiente virtual
  ```sh
$   env/Scripts/activate
  ```
Instalar as dependências
```sh
$   pip install -r requirments.txt
```
Preparar migração do banco
```sh
$   python manage.py makemigrations
```
Migrar o banco de dados
```sh
$   python manage.py migrate
```
Rodar o django
```sh
$   python manage.py runserver
```
 
# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
