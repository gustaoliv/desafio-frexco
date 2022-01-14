# Desafio Tech (Python)

- Criar uma API usando a linguagem Python, frameworks: Django e Django Rest Framework.
- A API deverá realizar a comunicação com um banco de dados SQL qualquer (pode ser SQLite)
- O banco deverá ter pelo menos duas tabelas: 
         - Uma tabela chamada “Region” que conterá apenas uma coluna “name” com informação dos nomes das regiões do Brasil ( Norte, Nordeste, etc.)
         - Uma tabela chamada “Fruit” que conterá colunas “name” (o nome da fruta) e uma coluna de associação por chave estrangeira (foreign key) com a tabela “Region” associando cada fruta a uma região existente na primeira tabela.
- Para cada tabela, a API deve conter os quatro métodos GET, POST, PUT e DELETE.


# Acesso a API
- Rota: ```localhost/api/```
- Acesso aos métodos: podem ser feitos utilizando o Postman por exemplo, os métodos **GET** e **POST** podem ser executados diretamente no browser, pelas rotas:
  - ```localhost/api/region/```
  - ```localhost/api/fruit/```
  
# Pacotes e Ferramentas Utilizados
- PostgreSQL 14.1
- Django 4.0.1
- Django Rest Framework 3.13.1
- Psycopg2 2.9.3