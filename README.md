# MTVFirstProject

Projeto de estudo para praticar os fundamentos do **Django** e o padrão **MTV** (Model, Template, View). Foi feito como primeiro contato com o framework e não tem a pretensão de ser um produto final.

## O que o projeto faz

Simula a base de um sistema simples de restaurante:

- Uma página com um **formulário de reserva** (nome, sobrenome, e-mail, número de convidados e comentários), que salva os dados no banco.
- Duas rotas simples de "Hello" para testar views baseadas em função e em classe.
- Painel administrativo do Django com o model de reservas registrado.
- Um model de cardápio (`MenuItem`) já criado, ainda sem views ou telas.

## Rotas

| Rota            | O que faz                                                        |
|-----------------|------------------------------------------------------------------|
| `/`             | Retorna "Hello World" (view baseada em função)                   |
| `/brasil/`      | Retorna "Hello Brazil" (view baseada em classe, `View`)          |
| `/reservation`  | Exibe o formulário de reserva e salva no banco ao enviar (POST)  |
| `/admin/`       | Painel administrativo do Django                                  |

## Tecnologias

- Python 3.14
- Django 6.1
- MySQL (o Django 6.1 exige **MySQL 8.4 ou superior**)
- mysqlclient (driver do MySQL para o Django)
- python-dotenv (leitura das credenciais a partir do arquivo `.env`)

## Como rodar localmente

**1. Clone o repositório e entre na pasta**

```bash
git clone <url-do-repositorio>
cd MTVFirstProject
```

**2. Crie e ative o ambiente virtual**

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install django mysqlclient python-dotenv
```

**4. Crie o banco de dados no MySQL**

```sql
CREATE DATABASE django_db;
```

**5. Configure as credenciais no arquivo `.env`**

O projeto **não guarda senhas no código**: a `SECRET_KEY` e os dados de conexão com o MySQL são lidos de um arquivo `.env`. Ele não vem no repositório, então **é necessário criá-lo e preencher as suas credenciais** antes de rodar o projeto (se você ainda não fez isso).

Dentro da pasta `mtvproject/` (a mesma do `manage.py`), copie o modelo `.env.example` para `.env`:

```bash
cd mtvproject

# Windows (PowerShell)
Copy-Item .env.example .env

# Linux / macOS
cp .env.example .env
```

Depois edite o `.env` com os seus valores:

```
SECRET_KEY='sua-chave-secreta'
DB_NAME=django_db
DB_USER=root
DB_PASSWORD=sua_senha_do_mysql
DB_HOST=127.0.0.1
DB_PORT=3306
```

Para gerar uma `SECRET_KEY` nova:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Se alguma variável obrigatória (`SECRET_KEY` ou `DB_PASSWORD`) estiver faltando, o Django mostra um `KeyError` ao iniciar.

**6. Aplique as migrações e (opcionalmente) crie um superusuário**

```bash
python manage.py migrate
python manage.py createsuperuser
```

**7. Suba o servidor**

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/reservation` para ver o formulário, ou `http://127.0.0.1:8000/admin/` para o painel administrativo.

## Estrutura do projeto

```
MTVFirstProject/
└── mtvproject/
    ├── manage.py
    ├── .env.example         # modelo das credenciais (copie para .env)
    ├── mtvproject/          # configurações do projeto (settings, urls raiz)
    └── firstapp/            # app principal
        ├── models.py        # MenuItem e Reservetion
        ├── forms.py         # ReservetionForm (ModelForm)
        ├── views.py         # views de exemplo e view do formulário
        ├── urls.py          # rotas do app
        ├── admin.py         # registro no admin
        ├── templates/
        │   └── index.html   # template do formulário
        └── migrations/
```

## Observações

- Projeto **exclusivamente de estudo**: não está pronto para produção (`DEBUG = True`, sem testes automatizados).
- Depois de salvar uma reserva, a view apenas devolve uma mensagem simples de sucesso, sem redirecionamento nem tela de confirmação.
- O nome do model `Reservetion` foi mantido como está, por ter sido criado assim no início do estudo.
