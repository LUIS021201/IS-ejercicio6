import json

def abrir_archivo_json(archivo):
    try:
        with open(archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{archivo}' no se encontró.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al decodificar el archivo JSON '{archivo}': {e}")


