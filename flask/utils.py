import re

participants = []

def validar_nom(nom):
    # Eliminar espacios innecesarios (más de un espacio entre palabras se reemplaza por uno solo)
    nom = re.sub(r'\s+', ' ', nom).strip()

    # Comprobar si el nombre no es solo números y contiene al menos una letra
    if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ0-9]+(?: [A-Za-zÁÉÍÓÚáéíóúñÑ0-9]+)*$', nom) and not nom.isdigit():
        return True
    else:
        return False
