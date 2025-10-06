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

elif menu == "Listar":
    st.subheader("Listar Alunos Cadastrados")
    alunos = cd.listar_aluno()
    if alunos:
        for linha in alunos:
            st.write(f"ID: {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]}")
    else:
        st.warning("Nenhum aluno encontrado")

elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = cd.listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Escolha o id do aluno para atualizar", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=16, step=1)
        if st.button("Atualizar"):
            cd.atualizar_idade(id_aluno, nova_idade)
            st.success("Idade atualizada com sucesso")
    else:
        st.info("Nenhum aluno disponível para atualizar")

elif menu == "Deletar":
    st.subheader("Deletar Alunos")
    alunos = cd.listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Escolha o ID do aluno para remover", [linha[0] for linha in alunos])
        if st.button("Deletar"):
            cd.deletar_aluno(id_aluno)
            st.success("Aluno deletado com sucesso")
    else:
        st.info("Nenhun aluno registrado na lista")