================================
 Passos para criar um projeto
================================


Bullet Lists
-------------

1. Virtual Enviroment

  * Criar com python especifico(2.7): mkvirtualenv --python /usr/bin/python2.7 NOME_DO_ENV 
  * Entrar: workon NOME_DO_ENV
  * Sair: deactivate

2. Instalar Django

  * Estando dentro da Venv

  * pip install django==VERSÃO
  	+ pip será o comando que instalará tudo dentro da venv.

3. Criando repositório

  * Acesse https://git.znc.com.br/
  * Se gerada nova SSH, adicionar
  * New project

4. Global Settings

  * git config --global user.name "SEU NOME"

  * git config --global user.email "SEU@EMAIL.COM"

5. Clonando repositório

  * git clone SEU@EMAIL.COM:USUARIO/NOME_DO_PROJETO.git

6. Usando pasta existente ou um repósitrio já criado

  * cd PASTA_DO_PROJETO

  * git init

  * git remote add origin git@git.znc.com.br:USUARIO/
  NOME_DO_PROJETO.git
  Estando dentro da Venv

7. Commitando

  * cd PASTA_DO_PROJETO

  * git status

  * git add .

  * git status

  * git commit -m "MENSAGEM DO COMMIT"

  * git push -u origin master

8. Criando o projeto

  * django-admin startproject NOME_DO_PROJETO .
  	+ Sem o ponto no final um novo diretório com o nome do projeto será criado

9. Configurando settings.py do projeto

  * Adicionar o path do STATIC_ROOT: 
  	+ STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  * Configuração do timezone:
  	+ TIME_ZONE = 'America/Sao_Paulo'

10. Criando banco de dados

  * Estando dentro da Venv
  
  * Estando dentro do diretório do projeto

  * python manage.py migrate

11. Rodando o servidor
  
  * O terminal que rodar o servidor ficará inutilizado para outras tarefas

  * Estando dentro da venv

  * Estando dento do diretório do projeto

  * python manage.py runserver

12. Criando aplicação
  
  * python manage.py startapp NOME_DA_APLICAÇÃO

  * No arquivo NOME_DO_PROJETO/settings.py adicionar a aplicação em INSTALLED_APPS

  * Para adicionar inclua abaixo a ultima instrução: 'NOME_DA_APLICAÇÃO',
