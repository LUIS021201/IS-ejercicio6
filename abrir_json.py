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




def escribir_en_archivo_json(archivo, datos):
    try:
        with open(archivo, 'w') as file:
            json.dump(datos, file, indent=4)
        print(f"Los datos se han escrito en el archivo '{archivo}' correctamente.")
    except Exception as e:
        print(f"Error al escribir en el archivo JSON '{archivo}': {e}")

# Ejemplo de uso:
datos_a_escribir = {"nombre": "Juan", "edad": 30, "ciudad": "Ejemploville"}
archivo_destino = "datos.json"

escribir_en_archivo_json(archivo_destino, datos_a_escribir)

