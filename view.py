import sqlite3 as lite

con = lite.connect('dados.db')


# inserir

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query,i)




# acessar informações

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista

# Atualizando informação

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)


# Deletar
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)

