import json

def abrir_archivo_json(archivo):
    try:
        with open(archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON '{archivo}': {e}")
        return None

# Ejemplo de uso:
datos = abrir_archivo_json("archivo_inexistente.json")
if datos is not None:
    print("Datos del archivo JSON:", datos)


