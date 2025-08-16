import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..','datos', 'db.json')

def guardar_cliente(cliente):
    cc=cliente["cc"]
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = {"clientes": {}}
    if not isinstance(datos.get("clientes"), dict):
        datos["clientes"] = {}
    datos["clientes"][cc]=cliente

    with open(DB_PATH, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo)

def consultar_cliente(cc):
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    clientes = datos.get("clientes", {})
    return clientes.get(cc)
    
