# 💳 Sistema de Cuentas Bancarias con JSON

---

## 👤 Autor

**Manuel Jose Gomez Laiton**

---

## 📝 Descripción

Este proyecto es una implementación de un sistema de cuentas bancarias con persistencia en archivos JSON. Permite la gestión de clientes, cuentas, CDTs y créditos, junto con operaciones de consulta y modificación sobre los datos almacenados.

---

## 🧑‍💻 Stack Tecnológico

- **Python 3.x**

---

## ⚙️ Requerimientos

- Python 3.x instalado
- Sistema operativo: Linux o Windows

---

## 🚀 Ejecución : ¿Cómo se ejecuta su proyecto?

### 🐧 Linux

```bash
python main.py
```

### 🖥️ Windows

```bash
python main.py
```

---

## 📁 Estructura de Archivos

```
cuentas_bancarias_implementacion_json/
│
├── main.py                                 #Codigo principal
├── datos/
│   └── db.json                             #Base de datos 
└── Modulos/
    ├── creacion_Clientes.py                #Logica de todo lo que entra relacionado con clientes
    ├── creacion_Cuentas.py                 #Logica de todo lo relacionado a las cuentas(creacion e historiales)
    ├── creditos.py                         #Logica de la creacion de creditos y su manejo
    ├── persistencia.py                     #Logica para manejo de datos JSON
    └── menus.py                            #Interface de menus
```
---

## 🗄️ Ejemplo de Base de Datos (`db.json`)

```json
{
  "clientes": {
    "cc": {
      "cc": "string",
      "nombre": "string",
      "email": "string",
      "edad": "string",
      "contacto": {
        "movil": "string",
        "fijo": "string"
      },
      "ubicacion": {
        "pais": "string",
        "departamento": "string",
        "ciudad": "string",
        "direccion": "string"
      },
      "cuentas": {
        "ahorros": {
          "numero": "string",
          "saldo": "number",
          "movimientos": [
            {
              "fecha": "string (YYYY-MM-DD)",
              "tipo": "string",
              "monto": "number",
              "descripcion": "string"
            }
          ]
        }
      },
      "CDT": {
        "cdt_id": {
          "monto": "number",
          "fecha_apertura": "string (YYYY-MM-DD)",
          "plazo_meses": "number",
          "tasa_interes": "number",
          "estado": "string",
          "historial": [
            {
              "fecha": "string (YYYY-MM-DD)",
              "accion": "string",
              "descripcion": "string"
            }
          ]
        }
      },
      "creditos": {
        "credito_id": {
          "monto": "number",
          "fecha_aprobacion": "string (YYYY-MM-DD)",
          "plazo_meses": "number",
          "tasa_interes": "number",
          "estado": "string",
          "saldo_pendiente": "number",
          "historial": [
            {
              "fecha": "string (YYYY-MM-DD)",
              "accion": "string",
              "monto": "number",
              "descripcion": "string"
            }
          ]
        }
      }
    }
  }
}
```

---

---

## 🛠️ Funcionalidades

- **Gestión de clientes:**  
  Permite crear, consultar y almacenar información de clientes, incluyendo sus datos personales y de contacto.

- **Gestión de cuentas bancarias:**  
  Creación de cuentas de ahorro y corriente, consulta de saldos y movimientos.

- **Gestión de CDTs:**  
  Permite la apertura y consulta de Certificados de Depósito a Término (CDT), cálculo de ganancias y plazos.

- **Gestión de créditos:**  
  Registro y consulta de créditos otorgados a los clientes, control de pagos y deudas.

- **Persistencia de datos:**  
  Todos los datos se almacenan en archivos JSON para asegurar la integridad y recuperación de la información.

- **Historial de movimientos:**  
  Consulta detallada de los movimientos realizados en cuentas, créditos y CDTs de cada cliente.

---

---

## 📦 Librerías Externas

- Ninguna (solo se utilizan librerías estándar de Python como `json` y `os`)

---
