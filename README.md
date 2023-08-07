# Teste Prático - Desenvolvedor

Este é um exemplo de aplicativo API construído com Python e Flask.

## Configuração

1. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Copie o env de example e gere uma key

```bash
cp .env.example .env
python app/console/commands/generate_key.py
```

## Migrações de Banco de Dados

Para criar e aplicar migrações de banco de dados, execute o seguinte comando:

```bash
alias flask='python -m flask'
flask db init
flask db migrate
flask db upgrade
```

## Execução

Para executar o aplicativo, use o seguinte comando:

```bash
flask run
```

O aplicativo estará disponível em http://localhost:5000.

## Rotas

- /api/users - Rota para criar um novo usuário (POST).
- /api/users/<id> - Rota para visualizar, atualizar ou excluir um usuário (GET, PUT, DELETE).

Rotas protegidas por autenticação JWT (PUT, DELETE).

## Autenticação

Para autenticar, faça uma solicitação POST para /api/auth/login com um JSON no corpo da solicitação contendo as informações de autenticação (username e password). Isso retornará um token JWT que pode ser usado para acessar rotas protegidas.
