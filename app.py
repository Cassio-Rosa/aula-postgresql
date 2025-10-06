import streamlit as st
import crud as cd

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="👨‍🎓")

st.title("Sistema de alunos usando o PostgreSQL")

menu = st.sidebar.radio("Menu", ["inserir", "Listar", "Atualizar", "Deletar"])

if menu == "inserir":
    st.subheader("➕ Adicionar Alunos")
    nome = st.text_input("Nome", placeholder="Insira o nome")
    idade = st.number_input("Idade", min_value=16, step=1)
 
    if st.button("Cadastrar"):
        if nome.strip() != "":
            cd.criar_aluno(nome,idade)
            st.success(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo nome pode estar vazio.")
