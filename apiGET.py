from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la conexión a la base de datos
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar a la base de datos", e)
        return None

# Ruta para obtener todos los registros de la tabla Curso
@app.route('/api/v1/cursos', methods=['GET'])
def get_cursos():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM curso")
        cursos = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(cursos)
    else:
        return jsonify({"error": "Error en la conexión a la base de datos"}), 500

if __name__ == '__main__':
    app.run(debug=True)