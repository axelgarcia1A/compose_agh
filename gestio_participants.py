from utils import validar_nom, participants
import json

# Puntuaciones globales
puntuacions = {}

# Función para agregar un participante
def afegir_participant(nom):
    nom = nom.strip()  # Limpia espacios al inicio y final
    if validar_nom(nom):  # Valida que el nombre contenga solo letras
        participants.append(nom)  # Añadir participante a la lista
        print(f"Participant registrat: {nom}")
    else:
        print('ERROR: El nombre introducido no es válido. Introduce un nombre que solo contenga letras.')

# Función para guardar los participantes en un archivo JSON
def desar_participants_a_fitxer(participants, fitxer):
    try:
        with open(fitxer, 'w') as f:
            json.dump(participants, f)  # Guardar la lista de participantes en formato JSON
        print("Participantes guardados en el archivo.")
    except Exception as e:
        print(f"Error al guardar los participantes: {e}")

# Función para cargar los participantes desde un archivo JSON
def carregar_participants_de_fitxer(filename='participants.json'):
    try:
        with open(filename, 'r') as file:
            participants = json.load(file)  # Cargar la lista de participantes desde el archivo
        return participants
    except FileNotFoundError:
        return []  # Si no se encuentra el archivo, devuelve una lista vacía
    except json.JSONDecodeError:
        return []  # Si el archivo no es un JSON válido, devuelve una lista vacía
    except Exception as e:
        print(f"Error al cargar los participantes: {e}")
        return []  # En caso de error, devuelve una lista vacía
