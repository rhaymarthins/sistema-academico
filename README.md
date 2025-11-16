# Sistema de Gerenciamento Acadêmico
Este é um projeto Django para gerenciamento de matrículas de alunos em cursos acadêmicos.

---

## ✅ Pré-requisitos

- **Python 3.9** instalado ou superior  
- **PostgreSQL** (ou outro banco de dados de sua preferência)

---

## 🚀 Passo a Passo para Configuração do Projeto


### 1. Criar e Ativar Ambiente Virtual

```bash
# Criar ambiente virtual
python3 -m venv ./venv

# Ativar ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate
```

---

### 2. Instalar Dependências

```
# Instalar Django
pip install django

# Instalar psycopg2 para conexão com PostgreSQL
pip install psycopg2
pip install psycopg2-binary

```

---

### 3. Configurar Banco de Dados

Edite o arquivo academico/settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Executar Migrações

```
# Criar migrações baseadas nos modelos
python manage.py makemigrations

# Aplicar migrações ao banco de dados
python manage.py migrate
```

### 5. Coletar Arquivos Estáticos

```
python manage.py collectstatic
```

### 6. Executar Servidor de Desenvolvimento
```
python manage.py runserver
```