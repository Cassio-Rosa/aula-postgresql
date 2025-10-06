# 👨‍🎓 Sistema de Gerenciamento de Alunos

Este é um sistema simples para gerenciar alunos usando **Python**, **PostgreSQL** e **Streamlit**.  
Com ele, é possível **inserir**, **listar**, **atualizar** e **deletar** alunos de um banco de dados.

---

## ⚙️ Funcionalidades

- ➕ Inserir aluno  
- 📋 Listar alunos  
- ✏️ Atualizar idade  
- 🗑️ Deletar aluno  

---

## 🧩 Tecnologias utilizadas

- Python 3  
- Streamlit  
- PostgreSQL  
- psycopg2  

---

## 🗄️ Estrutura do projeto

crud.py → Funções CRUD (criar, listar, atualizar, deletar)
app.py → Interface do Streamlit
db.py → Conexão com o banco PostgreSQL

yaml
Copiar código

---

## 🚀 Como executar

1. Crie a tabela no PostgreSQL:
   ```sql
   CREATE TABLE alunos (
       id SERIAL PRIMARY KEY,
       nome VARCHAR(100),
       idade INT
   );
Configure o arquivo db.py com suas credenciais do banco de dados.

Instale as dependências:

bash
Copiar código
pip install streamlit psycopg2
Execute o sistema:

bash
Copiar código
streamlit run app.py
