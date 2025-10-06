# 👨‍🎓 Sistema de Gerenciamento de Alunos

Um sistema CRUD completo desenvolvido em **Python** com **Streamlit** e **PostgreSQL**, que permite cadastrar, listar, atualizar e deletar alunos de um banco de dados de forma prática e interativa.

---

## 🧠 Sobre o Projeto

O objetivo deste projeto é demonstrar o uso de **operações CRUD** (Create, Read, Update, Delete) com banco de dados **PostgreSQL**, integrando tudo em uma **interface web simples** feita com o **Streamlit**.

---

## ⚙️ Funcionalidades

✅ **Adicionar aluno** – Insere um novo aluno no banco.  
📋 **Listar alunos** – Exibe todos os alunos cadastrados.  
✏️ **Atualizar idade** – Permite atualizar a idade de um aluno existente.  
🗑️ **Deletar aluno** – Remove um aluno pelo ID.  

---

## 🧩 Tecnologias Utilizadas

- **Python 3**  
- **Streamlit** – Interface web  
- **PostgreSQL** – Banco de dados relacional  
- **psycopg2** – Conexão entre Python e PostgreSQL  

---

## 🗂️ Estrutura do Projeto

📁 projeto_alunos
|
├── crud.py → Funções CRUD (criar, listar, atualizar, deletar)
|
├── app.py → Interface principal com Streamlit
|
├── db.py → Configuração e conexão com o banco de dados
|
└── README.md → Documentação do projeto

yaml
Copiar código

---

## ⚡ Como Executar o Projeto

### 1️⃣ Criar a tabela no PostgreSQL
Antes de rodar o sistema, crie o banco de dados e a tabela de alunos:

```sql
CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL
);
2️⃣ Configurar a conexão com o banco
No arquivo db.py, defina suas credenciais do PostgreSQL:

python
Copiar código
import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="seu_banco",
            user="seu_usuario",
            password="sua_senha"
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro na conexão: {erro}")
        return None, None
3️⃣ Instalar as dependências
Instale as bibliotecas necessárias:

bash
Copiar código
pip install streamlit psycopg2
4️⃣ Executar o sistema
Inicie o Streamlit com o comando:

bash
Copiar código
streamlit run app.py
Após isso, o sistema abrirá automaticamente no navegador (geralmente em: http://localhost:8501).
```

🧑‍💻 Autor
Desenvolvido por Cássio Rosa
💡 Projeto criado para fins de aprendizado e prática com Python, SQL e Streamlit.


