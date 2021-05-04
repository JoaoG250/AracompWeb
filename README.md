# AracompWeb

Projeto da aplicação web para o Aracomp 2021 em Django

## Dependências

* Python 3.8
* pip

## Instruções de instalação

### Instalação do pipenv

execute o comando: `pip install pipenv`

1. Instale as dependências do python com o pipenv:

``` bash
python -m pipenv shell
pipenv install
```

1. Entre na pasta do projeto Django: `cd aracomp`
1. Faça as migrações do banco de dados embarcado: `python manage.py migrate`
1. Execute o servidor: `python manage.py runserver`
1. Após a execução remova o ambiente virtual com o comando: pipenv --rm
1. Saia do ambiente com o comando: exit
