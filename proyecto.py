from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Lista de tareas:
# Cada tarea es un diccionario con 'id', 'texto' y 'hecho' (booleano)
tareas = []
siguiente_id = 1

def agregar_tarea(texto):
    """Añade una nueva tarea a la lista."""
    global siguiente_id
    nueva_tarea = {
        'id': siguiente_id,
        'texto': texto,
        'hecho': False
    }
    tareas.append(nueva_tarea)
    siguiente_id += 1

def completar_tarea(id_tarea):
    """Marca una tarea como completada o incompleta según su estado actual."""
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['hecho'] = not tarea['hecho']
            break

@app.route('/')
def index():
    # Ordenar tareas: incompletas (False) primero, luego completadas (True)
    # sorted() ordena de forma ascendente por defecto, por lo que False va antes que True
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    # Para que funcione, también necesitas un archivo `index.html` en una carpeta `templates`
    # app.run(debug=True)
    # Usa app.run() si no necesitas el modo debug
    app.run()