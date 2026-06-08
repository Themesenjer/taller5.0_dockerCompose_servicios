from flask import Flask
import psycopg2

app = Flask(__name__)

VERSION = "2.0.0"


@app.route("/")
def inicio():

    try:

        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()

        # Obtener clientes
        cursor.execute("SELECT id, nombre FROM clientes;")
        clientes = cursor.fetchall()

        lista_clientes = ""

        for cliente in clientes:
            lista_clientes += f"<li>{cliente[0]} - {cliente[1]}</li>"

        cursor.close()
        conexion.close()

        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>

        <p>Conexión exitosa a PostgreSQL</p>

        <h3>Clientes registrados</h3>

        <ul>
            {lista_clientes}
        </ul>
        """

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)