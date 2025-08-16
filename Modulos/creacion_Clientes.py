import json
import os
from typing import Dict, List, Optional
from Modulos.persistencia import guardar_cliente
from Modulos.persistencia import consultar_cliente
db="Modulos/db.json"
clientes={}



def crear_clientes():

    cc = input("Ingrese el número de cédula del cliente: ")
    if cc in clientes:
        print("El cliente ya existe.")
        return
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    name= input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    if '@' not in email or '.' not in email:
        print("El correo electrónico no es válido.")
        return
    age= int(input("Ingrese la edad del cliente: "))
    if age < 18:
        print("El cliente debe ser mayor de edad.")
        return
     
    contacto = int(input("¿Qué medio de comunicación prefiere?\n1. Móvil\n2. Fijo\n3. Ambos\n"))

    if contacto == 1:
        telefono = input("Ingrese el número de teléfono móvil: ")
        if not telefono.isdigit() or len(telefono) != 10:
            print("El número de teléfono móvil debe contener al menos 10 dígitos.")
            return
        contacto_telefonico = {"movil": telefono}

    elif contacto == 2:
        telefono = input("Ingrese el número de teléfono fijo: ")
        if not telefono.isdigit() or len(telefono) > 7:
            print("El número de teléfono fijo debe contener al menos 7 dígitos.")
            return
        contacto_telefonico = {"fijo": telefono}

    elif contacto == 3:
        telefono_movil = input("Ingrese el número de teléfono móvil: ")
        if not telefono_movil.isdigit() or len(telefono_movil) < 10:
            print("El número de teléfono móvil debe contener al menos 10 dígitos.")
            return
        telefono_fijo = input("Ingrese el número de teléfono fijo: ")
        if not telefono_fijo.isdigit() or len(telefono_fijo) < 7:
            print("El número de teléfono fijo debe contener al menos 7 dígitos.")
            return
        contacto_telefonico = {
            "movil": telefono_movil,
            "fijo": telefono_fijo
        }
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return
    pais = input("Ingrese el país del cliente: ")
    if not pais.isalpha():
        print("El país debe contener solo letras.")
        return
    depatartamento = input("Ingrese el departamento del cliente: ")
    if not depatartamento.isalpha():
        print("El departamento debe contener solo letras.")
        return
    ciudad = input("Ingrese la ciudad del cliente: ")   
    if not ciudad.isalpha():
        print("La ciudad debe contener solo letras.")
        return
    direccion = input("Ingrese la dirección del cliente: ")
    if not direccion:
        print("La dirección no puede estar vacía.")
        return
    

    clientes[cc] = {
        "cc": cc,
        "nombre": name,
        "email": email,
        "edad": age,
        "contacto": contacto_telefonico,
        "ubicacion": {"pais": pais, "departamento": depatartamento, "ciudad": ciudad, "direccion": direccion},
        "cuentas": {},
        "creditos": {}
    }
    print(f'Cliente {name} creado exitosamente.')
    guardar_cliente(clientes[cc])
    

def consultar_clientes():
    cc = input("Ingrese el número de cédula del cliente a consultar: ").strip()
    cliente = consultar_cliente(cc)  # ✅ Llamada correcta

    if cliente:
        print(f"\nDatos del cliente {cc}:")
        for clave, valor in cliente.items():
            print(f"{clave}: {valor}")
    else:
        print(f"No se encontró ningún cliente con cédula {cc}.")
