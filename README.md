
# Auth API – Programa.AI (AppSec)

## ⚡ Visão Geral

Esta API fornece endpoints de autenticação e controle de acesso para aplicações que necessitam de:

- Registro de usuários
- Login (autenticação)
- Emissão e renovação de tokens (ex: JWT)
- Recuperação/alteração de senha
- Revogação de sessão / logout
- Hardening de segurança alinhado a boas práticas de AppSec

---

## 🧱 Stack / Tecnologias

| Tecnologia                                             | Uso Principal            | Observações                                                                                   |
| ------------------------------------------------------ | ------------------------ | ----------------------------------------------------------------------------------------------- |
| Python                                                 | Linguagem base           | Versão sugerida: 3.11+                                                                         |
| FastAPI ou Flask (TODO confirmar)                      | Framework web/API        | FastAPI é comum em APIs modernas pela tipagem e OpenAPI embutido                               |
| Mako                                                   | Template engine          | Pode ser usado para e-mails, páginas HTML de confirmação ou geração de conteúdo dinâmico |
| Docker / Docker Compose                                | Containerização        | Facilita o deploy consistente                                                                   |
| Shell Scripts                                          | Automação              | Inicialização, migrações ou tarefas utilitárias                                            |
| Banco de Dados (ex: PostgreSQL/MySQL/SQLite) (TODO)    | Persistência            | Defina a variável `DATABASE_URL`                                                             |
| ORM (ex: SQLAlchemy + Alembic) (TODO)                  | Modelagem + migrações  | Alembic para versionar o schema                                                                 |
| JWT (ex: PyJWT) (TODO)                                 | Tokens de autenticação | Segredo via `JWT_SECRET`                                                                      |
| Ferramentas de Segurança (ex: passlib, bcrypt) (TODO) | Hash de senha            | Nunca armazene senhas em texto puro                                                             |
| Testes (ex: pytest) (TODO)                             | Qualidade                | Cobrir fluxos críticos de auth                                                                 |

---

## 📁 Estrutura de Diretórios (Exemplo Proposto)

```
auth-api-programa-ai/
├─ app/
│  ├─ core/              # Configurações centrais (security, settings)
│  ├─ models/            # Modelos / ORM
│  ├─ schemas/           # Pydantic (request/response)
│  ├─ services/          # Regras de negócio (auth, email)
│  ├─ api/
│  │  ├─ v1/             # Rotas versão 1
│  ├─ templates/         # Templates Mako
│  └─ main.py            # Entry point (FastAPI/Flask app)
├─ migrations/ (Alembic) # Migrações de banco (TODO)
├─ scripts/              # Shell scripts utilitários
├─ tests/                # Testes automatizados (pytest)
├─ Dockerfile
├─ docker-compose.yml (TODO)
├─ requirements.txt / pyproject.toml
└─ README.md
```

Ajuste conforme a estrutura real do seu repositório.

---

## 🔐 Fluxo de Autenticação (Exemplo)

1. Usuário registra-se (email + senha).
2. Senha é hasheada (ex: bcrypt).
3. Usuário faz login → valida credenciais.
4. API emite JWT de acesso + (opcional) refresh token.
5. Rotas protegidas exigem header: `Authorization: Bearer <token>`.
6. Refresh token usado para renovar sessão sem re-login.
7. Logout (opcional) marca refresh token como revogado (se houver persistência de token).
8. Recuperação de senha envia e-mail usando template Mako.

---

## ⚙️ Pré-requisitos

- Python 3.11 ou superior
- Docker + Docker Compose (opcional porém recomendado)
- Make (opcional)
- Acesso às variáveis de ambiente adequadas

---

## 📦 Instalação (Modo Local – Sem Docker)

```bash
# 1. Clone
git clone https://github.com/Antoniolps/auth-api-programa-ai.git
cd auth-api-programa-ai

# 2. Crie ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instale dependências
pip install -r requirements.txt
# ou, se usar Poetry:
# poetry install

# 4. Configure .env
cp .env.example .env  # (Se existir) e edite

# 5. Execute migrações (se Alembic for usado)
alembic upgrade head  # (TODO confirmar uso)

# 6. Inicie a aplicação (FastAPI exemplo)
uvicorn app.main:app --reload --port 8000
```

Acesse: http://localhost:8000

Se FastAPI: documentação automática em http://localhost:8000/docs e http://localhost:8000/redoc.

---

## 🐳 Execução com Docker

Exemplo de `docker-compose.yml` (crie se não existir):

```yaml
version: "3.9"
services:
  api:
    build: .
    container_name: auth_api
    env_file: .env
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres:16
    container_name: auth_db
    environment:
      POSTGRES_USER: usuario
      POSTGRES_PASSWORD: senha
      POSTGRES_DB: authdb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

Rodar:

```bash
docker compose up --build
```

## 🛠 Comandos Úteis (Sugestões)

```bash
# Formatação e lint
ruff check .
ruff format .

# Migrações
alembic revision -m "descrição"
alembic upgrade head

# Rodar servidor
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🧾 Licença

Defina a licença (MIT, Apache-2.0, etc.) se ainda não houver. (TODO)

---

## ❓ Suporte / Dúvidas

Abra uma Issue no repositório ou entre em contato pelo canal do curso.

---

## 📝 Notas Finais

Este README contém partes genéricas baseadas em projetos típicos de autenticação em Python. Ajuste:

- Framework real (FastAPI vs Flask)
- ORM efetivamente utilizado
- Fluxo de e-mails / templates Mako
- Serviços externos (SMTP, Redis, etc.)

Se quiser, me informe os arquivos principais (ex: main.py, requirements.txt) para gerar um README totalmente aderente ao seu código.

Bom estudo e boas práticas de AppSec! 🔐
