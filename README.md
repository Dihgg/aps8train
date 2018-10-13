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
