from db import conectar

def criar_aluno(nome,idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
        "INSERT INTO alunos (nome, idade) VALUES (%s, %s) ",
        ("Cassio", "67")  
        )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()