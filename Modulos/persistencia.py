import json
import os

# Ruta absoluta al archivo db.json
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'datos', 'db.json')

# Cargar toda la base de datos
def cargar_db():
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            if not isinstance(datos.get("clientes"), dict):
                datos["clientes"] = {}
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        return {"clientes": {}}

# Guardar toda la base de datos
def guardar_db(db):
    with open(DB_PATH, "w", encoding="utf-8") as archivo:
        json.dump(db, archivo, indent=4)



# Guardar un cliente individual
def guardar_cliente(cc, cliente):
    db = cargar_db()
    db["clientes"][cc] = cliente
    guardar_db(db)


# Consultar un cliente por cédula
def consultar_cliente(cc):
    db = cargar_db()
    return db["clientes"].get(cc)
