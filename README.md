# Gerenciamento de Produtos - CRUD

Um sistema completo de **Gerenciamento de Produtos** construído com **FastAPI** no backend e **Streamlit** no frontend. O projeto demonstra operações CRUD (Create, Read, Update, Delete) em uma arquitetura moderna com banco de dados PostgreSQL.

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido como parte da **Jornada de Dados** e implementa um sistema robusto para gerenciar produtos com as seguintes funcionalidades:

- ✅ **Criar** produtos com nome, descrição, preço, categoria e email do fornecedor
- ✅ **Listar** todos os produtos disponíveis
- ✅ **Buscar** detalhes de um produto específico
- ✅ **Atualizar** informações de produtos existentes
- ✅ **Deletar** produtos do banco de dados

## 🏗️ Arquitetura do Projeto

```
Projeto 2 CRUD/
├── backend/                    # API FastAPI
│   ├── main.py                # Aplicação principal
│   ├── models.py              # Modelos SQLAlchemy
│   ├── schemas.py             # Schemas Pydantic (validação)
│   ├── database.py            # Configuração do banco de dados
│   ├── crud.py                # Operações CRUD
│   ├── router.py              # Rotas da API
│   └── requirements.txt        # Dependências do backend
│
├── frontend/                   # Interface Streamlit
│   ├── app.py                 # Aplicação Streamlit
│   └── requirements.txt        # Dependências do frontend
│
├── .env.example               # Exemplo de variáveis de ambiente
├── .gitignore                 # Arquivo de ignição do Git
└── README.md                  # Este arquivo
```

## 🚀 Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **Python-dotenv** - Gerenciamento de variáveis de ambiente
- **Uvicorn** - Servidor ASGI

### Frontend
- **Streamlit** - Framework para criar aplicações web interativas
- **Pandas** - Manipulação e análise de dados
- **Requests** - Cliente HTTP

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gerenciador de pacotes Python)

## ⚙️ Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-2-crud.git
cd "Projeto 2 CRUD"
```

### 2. Configure o arquivo `.env`

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com seus dados do PostgreSQL:

```env
POSTGRES_DB=seu_banco_de_dados
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=postgres  # Use 'localhost' se não usar Docker
```

### 3. Instale as dependências do Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Instale as dependências do Frontend

```bash
cd ../frontend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

## 🏃 Executando o Projeto

### Opção 1: Localmente (sem Docker)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # ou venv\Scripts\activate no Windows
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`
- Documentação interativa: `http://localhost:8000/docs`
- Documentação alternativa: `http://localhost:8000/redoc`

**Terminal 2 - Frontend:**
```bash
cd frontend
source venv/bin/activate  # ou venv\Scripts\activate no Windows
streamlit run app.py
```

A aplicação Streamlit estará disponível em: `http://localhost:8501`

### Opção 2: Com Docker Compose

```bash
docker-compose up --build
```

**URLs:**
- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:8501`

## 📚 Estrutura do Banco de Dados

### Tabela: `products`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer | ID único do produto (chave primária) |
| `name` | String | Nome do produto |
| `description` | String | Descrição detalhada |
| `price` | Float | Preço do produto |
| `categoria` | String | Categoria (Eletrônico, Eletrodoméstico, etc) |
| `email_fornecedor` | String | Email do fornecedor (validado) |
| `created_at` | DateTime | Data/hora de criação |

## 🔌 API Endpoints

### Obter todos os produtos
```
GET /products/
```
**Resposta (200):**
```json
[
  {
    "id": 1,
    "name": "Notebook",
    "description": "Notebook de alto desempenho",
    "price": 3500.00,
    "categoria": "Eletrônico",
    "email_fornecedor": "contato@empresa.com",
    "created_at": "2026-11-02T10:30:00"
  }
]
```

### Obter um produto específico
```
GET /products/{product_id}
```

### Criar novo produto
```
POST /products/
Content-Type: application/json

{
  "name": "Monitor",
  "description": "Monitor 27 polegadas",
  "price": 1200.00,
  "categoria": "Eletrônico",
  "email_fornecedor": "fornecedor@empresa.com"
}
```

### Atualizar produto
```
PUT /products/{product_id}
Content-Type: application/json

{
  "name": "Monitor 29\"",
  "price": 1500.00
}
```

### Deletar produto
```
DELETE /products/{product_id}
```

## 💻 Interface do Streamlit

A aplicação frontend oferece uma interface intuitiva com:

1. **Adicionar Produto** - Formulário para inserir novos produtos
2. **Visualizar Produtos** - Tabela com todos os produtos cadastrados
3. **Buscar Produto** - Pesquisar por ID
4. **Atualizar Produto** - Modificar dados de produtos existentes
5. **Deletar Produto** - Remover produtos do banco

## 🧪 Testando a API

Use ferramentas como **Postman** ou **curl** para testar os endpoints:

```bash
# Obter todos os produtos
curl http://localhost:8000/products/

# Criar um novo produto
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Mouse","description":"Mouse wireless","price":50.00,"categoria":"Eletrônico","email_fornecedor":"vendas@empresa.com"}'

# Obter um produto específico
curl http://localhost:8000/products/1

# Atualizar um produto
curl -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"price":55.00}'

# Deletar um produto
curl -X DELETE http://localhost:8000/products/1
```

## 📖 Documentação da API

Quando o backend está rodando, acesse a documentação interativa do Swagger:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## 🛡️ Validações

O projeto implementa validações robustas:
- ✓ Email do fornecedor (validação de formato)
- ✓ Preço positivo obrigatório
- ✓ Todos os campos são obrigatórios
- ✓ Campos de texto não podem estar vazios

## 📝 Variáveis de Ambiente

As seguintes variáveis de ambiente são necessárias (veja `.env.example`):

```env
POSTGRES_DB=produtos_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_segura
POSTGRES_HOST=postgres
```

## 🐛 Troubleshooting

### Erro de conexão com PostgreSQL
- Verifique se o PostgreSQL está rodando
- Confirme as credenciais no arquivo `.env`
- Verifique se o host está correto

### Streamlit não consegue conectar ao backend
- Certifique-se de que o backend está rodando na porta 8000
- Se usar Docker, ajuste o URL para `http://backend:8000`
- Se usar localhost, ajuste o URL para `http://localhost:8000`

### Erro de módulo não encontrado
- Ative o virtual environment correto
- Execute `pip install -r requirements.txt` novamente

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 👨‍💻 Autor

**Mateus Garcia**
- Email: mateusgarcia.br.mg@gmail.com
- GitHub: [@MateuS-Garci4](https://github.com/MateuS-Garci4)
