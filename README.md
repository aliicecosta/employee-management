# employee-management

Desafio Técnico Back-End.

## Descrição do Problema

&emsp; Desenvolver uma API para gerenciamento de colaboradores de uma empresa fictícia. A API deve ser integrada com um banco de dados e ser capaz de inserir, alterar e deletar usuários no banco.

### Requisitos obrigatórios

&emsp; Subir um banco de dados PostgreSQL com os seguintes dados dos funcionários:
* Nome
* Sobrenome
* Matrícula
* Cargo
* Código do Cargo
* Líder
* Matrícula do Líder
* Salário
* Senha
* Status do colaborador

&emsp; O desenvolvimento deve ser realizado com os seguintes requisitos obrigatórios:

| Requisito | Status |
|:---|:---:|
|Open API (também conhecido como Swagger) | Pendente
|Linguagem Python | Feito
|Flask | Feito
|Flask-restful ou Flask-RESTX | Feito
|Psycopg2 ou SQLAlchemy | Feito
|Clean Code | Feito
|Documentação do código (Docstring) e README | Feito
|Utilização do GIT | Feito
|Implementação de Testes Unitários (TDD) | Pendente

### Requisitos Opcionais

&emsp; Adicionalmente, para auxiliar positivamente na avaliação, pode-se utilizar:

| Requisito | Status |
|:---|:---:|
|Implementação de Teste de Integração (TDD) | Pendente |
|Implementação de Testes Funcionais (TDD) | Pendente |
|Docker | Feito |
|Docker compose | Feito



## Comentários

### Lista de pendências mapeadas:
* Verificação se o número de matrícula informado corresponde a um registro no banco (update, delete e get Employee);
* Adicionar um tabela de Cargos, com duas colunas: nome e código. Essa tabela seria utilizada para validar as informações inseridas;
* Verificar se o nome passado como líder de um novo colaborador existe no banco de dados:
    * Se sim, puxar automaticamente o número de matrícula;
    * Se não, indicar o erro;
* Criar uma rquivo main.py para inicializar o banco e subir executar a API;
* Melhorar a organização das pastas;
* ...

### API
&emsp; Testes da API foram realizados utilizando o Postman.

&emsp; Para coletar os dados salvos no banco, é possível selecionar apenas um colaborador ou todos.

&emsp; É possível alterar apenas um colaborador a cada requisição, podendo alterar um ou mais campos.

&emsp; Segue exemplos dos JSON de insert e update.

```python 
insert_data = {
    "registration" : 1,
    "name" : "João",
    "surname" : "Silva",
    "role": "Dev",
    "leader" : "Maria",
    "salary" : 7000.0,
    "password" : "123",
    "status" : true
}

update_data = {
    "registration" : 5,
    "args" : ["role", "salary"],
    "values" : ["Leader3", "10000.0"]
}
```

