from flask import Flask, render_template, request, redirect, url_for
from gestio_participants import afegir_participant, carregar_participants_de_fitxer, desar_participants_a_fitxer, participants
from gestio_partides import generar_partides, avançar_jornada, obtenir_resultats
from puntuacions import calcular_ranquing
import json

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal (home)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para gestionar los participantes
@app.route('/participants', methods=['GET', 'POST'])
def participants_view():
    if request.method == 'POST':
        participant_name = request.form.get('name')
        if participant_name:
            afegir_participant(participant_name)  # Llama a la función para agregar un participante
            desar_participants_a_fitxer(participants, 'participants.json')  # Guardar los participantes en un archivo JSON
            return redirect(url_for('participants_view'))  # Redirige para actualizar la lista de participantes
        else:
            print('El campo name está vacío o no existe.')
    participants_list = carregar_participants_de_fitxer('participants.json')  # Carga los participantes desde el archivo
    return render_template('participants.html', participants=participants_list)


# Ruta para generar y gestionar las partidas
@app.route('/partides', methods=['GET', 'POST'])
def partides_view():
    participants = carregar_participants_de_fitxer('participants.json')  # Cargar participantes desde el archivo
    if request.method == 'POST':
        # Generar las partidas cuando el usuario haga clic en el botón
        generar_partides(participants)
        resultats = avançar_jornada()  # Simular la jornada
        return render_template('partides.html', resultats=resultats)
    
    resultats = obtenir_resultats()  # Obtener resultados de las partidas
    return render_template('partides.html', resultats=resultats)

# Ruta para ver las puntuaciones y el ranking
@app.route('/puntuacions')
def puntuacions_view():
    # Cargar las puntuaciones desde el archivo o base de datos
    puntuacions = cargar_puntuacions()  # Esta función debe devolver un diccionario de puntuaciones
    ranking = calcular_ranquing(puntuacions)  # Llamar a calcular_ranquing pasando las puntuaciones
    return render_template('puntuacions.html', ranking=ranking)

# Función para cargar los participantes desde el archivo JSON
def cargar_participants():
    try:
        with open('participants.json', 'r') as file:
            participants = json.load(file)
    except FileNotFoundError:
        participants = []
    return participants

# Función para cargar las puntuaciones (deberías tener alguna forma de obtenerlas)
def cargar_puntuacions():
    try:
        with open('puntuacions.json', 'r') as file:
            puntuacions = json.load(file)
    except FileNotFoundError:
        puntuacions = {}
    return puntuacions

# Ruta para mostrar los participantes
@app.route('/mostrar_participants')
def mostrar_participants():
    # Cargar los participantes desde el archivo
    participants = cargar_participants()
    return render_template('participants.html', participants=participants)


if __name__ == '__main__':
    app.run(debug=True)
