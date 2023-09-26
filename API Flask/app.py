from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas em memória
tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna a lista de tarefas."""
    return jsonify({'tasks': tasks})


@app.route('/tasks', methods=['POST'])
def create_task():
    """Cria uma nova tarefa."""
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data['title']}
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente."""
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data['title']
            return jsonify({'task': task})
    return jsonify({'message': 'Tarefa não encontrada'}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Exclui uma tarefa existente."""
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Tarefa excluída'})
    return jsonify({'message': 'Tarefa não encontrada'}), 404


if __name__ == '__main__':
    app.run(debug=True)
