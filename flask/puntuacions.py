from gestio_participants import participants

# Función para actualizar las puntuaciones
def actualitzar_puntuacions(puntuacions, guanyador):
    # Actualiza la puntuación del ganador
    if guanyador in puntuacions:
        puntuacions[guanyador] += 1  # Aumenta la puntuación en 1 para el ganador
    else:
        puntuacions[guanyador] = 1  # Si el jugador no está en el diccionario, lo añade con puntuación 1
    print(f'Las puntuaciones actualizadas són: {puntuacions}')
    print(f'El guanyador ha sigut: {guanyador}')

# Función para calcular el ranking
def calcular_ranquing(puntuacions):
    # Asegúrate de que puntuacions no esté vacío
    if not puntuacions:
        print("No hay puntuaciones disponibles")
        return []

    # Ordenar las puntuaciones de mayor a menor
    punt_descending = sorted(puntuacions.items(), key=lambda item: item[1], reverse=True)
    print(f'El ranking calculado es: {punt_descending}')
    return punt_descending  # Devuelve una lista de tuplas (jugador, puntuación)
