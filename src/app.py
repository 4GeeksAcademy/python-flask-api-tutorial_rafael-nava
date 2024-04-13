from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
     # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)
    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    #Primero asegúrate de convertir el cuerpo de la solicitud en una estructura de datos real de Python, como un diccionario. Ya usamos request.json para eso
    request_body = request.json
    #Agrega el diccionario a la lista de todos
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    #Devuelve la lista actualizada todos al front end.
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Eliminas el elemento en la posición dada
    todos.pop(position)
    print("This is the position to delete:", position)
    # Retornas la lista actualizada en formato JSON
    return jsonify(todos)













# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)