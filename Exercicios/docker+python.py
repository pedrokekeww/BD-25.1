import mysql.connector

def main():
    # Ajuste os parâmetros conforme seu container
    conexao = mysql.connector.connect(
        host='127.0.0.1',      # ou o IP do host do Docker, se não for local
        port=3306,
        user='usuario',
        password='senhausuario',
        database='meubanco'
    )
    cursor = conexao.cursor()

    # Criação de tabela de exemplo
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100)
        )
    """)

    # Inserção de dados de exemplo
    cursor.execute("INSERT INTO pessoas (nome) VALUES ('Maria')")
    cursor.execute("INSERT INTO pessoas (nome) VALUES ('João')")
    conexao.commit()

    # Consulta de dados
    cursor.execute("SELECT * FROM pessoas")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()
