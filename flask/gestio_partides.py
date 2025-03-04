import random
import json

# Llista de partides
partides = []
puntuacions = {}

# Funció per generar partides automàticament entre els participants
def generar_partides(participants):
    global partides
    partides = []  # Reiniciar les partides a cada generació
    random.shuffle(participants)  # Barregem la llista de participants
    for i in range(0, len(participants), 2):
        if i + 1 < len(participants):
            partides.append((participants[i], participants[i + 1]))  # Crear parelles de jugadors
    return partides

# Funció per simular el resultat d'una partida
def simular_partida(jugador1, jugador2):
    # Simular qui guanya de manera aleatòria
    guanyador = random.choice([jugador1, jugador2])
    return guanyador

# Funció per avançar una jornada
def avançar_jornada():
    global puntuacions  # Asegurarse de que puntuacions se modifique
    resultats = []
    for partida in partides:
        guanyador = simular_partida(partida[0], partida[1])
        resultats.append((partida[0], partida[1], guanyador))
        
        # Actualizar puntuaciones
        if guanyador not in puntuacions:
            puntuacions[guanyador] = 0
        puntuacions[guanyador] += 1  # Aumentar puntos del ganador
        
    # Guardar las puntuaciones actualizadas en un archivo
    desar_puntuacions_a_fitxer(puntuacions)
    return resultats

# Funció per obtenir els resultats de totes les partides
def obtenir_resultats():
    resultats = []
    for partida in partides:
        guanyador = simular_partida(partida[0], partida[1])
        resultats.append((partida[0], partida[1], guanyador))
        
        # Actualizar puntuaciones
        if guanyador not in puntuacions:
            puntuacions[guanyador] = 0
        puntuacions[guanyador] += 1  # Aumentar puntos del ganador
        
    # Guardar las puntuaciones actualizadas en un archivo
    desar_puntuacions_a_fitxer(puntuacions)
    return resultats

# Función para guardar las partidas en un archivo
def desar_partides_a_fitxer(partides):
    with open("partides.json", "w") as file:
        json.dump(partides, file)

# Función para guardar las puntuaciones en un archivo
def desar_puntuacions_a_fitxer(puntuacions):
    with open("puntuacions.json", "w") as file:
        json.dump(puntuacions, file)

# Cargar las partidas desde el archivo
def carregar_partides_de_fitxer():
    try:
        with open("partides.json", "r") as file:
            partides = json.load(file)
    except FileNotFoundError:
        partides = []
    return partides

# Cargar las puntuaciones desde el archivo
def carregar_puntuacions_de_fitxer():
    try:
        with open("puntuacions.json", "r") as file:
            puntuacions = json.load(file)
    except FileNotFoundError:
        puntuacions = {}
    return puntuacions
