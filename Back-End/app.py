from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configuração de conexão com o banco de dados
db_config = {
    'host': os.getenv('DB_HOST', 'db'),  # Nome do serviço do container do banco de dados
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'challenge_db')
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Endpoint GET para obter todos os registros
@app.route('/points', methods=['GET'])
def get_points():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pontos_abastecimento")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

# Endpoint GET para obter um registro específico por ID
@app.route('/points/<int:id>', methods=['GET'])
def get_point_by_id(id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pontos_abastecimento WHERE id = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'Point not found'}), 404

# Endpoint POST para adicionar um novo registro
@app.route('/points', methods=['POST'])
def add_point():
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pontos_abastecimento (nome, rua, cidade, estado, tipo_carregador, capacidade) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (data['nome'], data['rua'], data['cidade'], data['estado'], data['tipo_carregador'], data['capacidade']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Point added successfully'}), 201

# Endpoint PUT para atualizar um registro existente por ID
@app.route('/points/<int:id>', methods=['PUT'])
def update_point(id):
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE pontos_abastecimento SET nome = %s, rua = %s, cidade = %s, estado = %s, tipo_carregador = %s, capacidade = %s WHERE id = %s",
                   (data['nome'], data['rua'], data['cidade'], data['estado'], data['tipo_carregador'], data['capacidade'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Point updated successfully'})

# Endpoint DELETE para remover um registro por ID
@app.route('/points/<int:id>', methods=['DELETE'])
def delete_point(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pontos_abastecimento WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Point deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
