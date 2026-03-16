# 🐍 Python AWS SDK

Configuración del entorno de desarrollo para utilizar el SDK de AWS para Python (Boto3).

---

## ▶️ Ejecutar el proyecto (main.py)

1. Asegúrate de tener tu entorno virtual activado (ver sección "Configuración del Entorno Virtual").

2. Ejecuta el script principal:

```bash
python main.py
```

> ⚠️ Si utilizas Windows y no tienes `python` en tu PATH, usa `python3` o la ruta completa al ejecutable de tu entorno virtual (por ejemplo, `.\.venv\Scripts\python.exe`).

## 🛠️ Configuración del Entorno Virtual

Para garantizar un aislamiento adecuado de las dependencias, es fundamental configurar un entorno virtual antes de comenzar.

### 📦 1. Crear el Entorno Virtual

Ejecuta el siguiente comando en la terminal desde la raíz de tu proyecto:

```bash
python -m venv .venv
```

---

### 🚀 2. Activar el Entorno Virtual

El comando de activación varía según el sistema operativo y el tipo de terminal que utilices:

#### 🪟 Windows

- **PowerShell:**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Símbolo del sistema (cmd):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

#### 🍎 macOS / 🐧 Linux

- **Bash / Zsh:**
  ```bash
  source .venv/bin/activate
  ```

---

### 🛑 3. Desactivar el Entorno

Cuando hayas terminado de trabajar, puedes salir del entorno virtual con:

```bash
deactivate
```

---

## 🔵 Comandos de AWS CLI - DynamoDB

Guía rápida para gestionar tablas y datos utilizando la interfaz de línea de comandos de AWS.

### 🏗️ 1. Gestión de Tablas

#### 🆕 1.1. Crear una Tabla

Para crear una tabla nueva, utiliza el comando `create-table`. Asegúrate de definir correctamente las claves y tipos de datos.

```sh
aws dynamodb create-table \
  --table-name 'Characters' \
  --attribute-definitions \
    'AttributeName=PK,AttributeType=S' \
  --key-schema \
    'AttributeName=PK,KeyType=HASH' \
  --provisioned-throughput \
     'ReadCapacityUnits=5,WriteCapacityUnits=5'
```

##### 📖 Desglose de Parámetros

| Propiedad (Prop)           | Nombre Técnico     | Descripción                                       | Notas de uso                                  |
| :------------------------- | :----------------- | :------------------------------------------------ | :-------------------------------------------- |
| `--table-name`             | Nombre             | Identificador único de la tabla.                  | Único por cuenta y región.                    |
| `--key-schema`             | Esquema de Clave   | Define los atributos de la clave primaria.        | `HASH` (Partition) o `RANGE` (Sort).          |
| `AttributeName`            | Atributo           | Nombre de la columna que es llave.                | Ejemplo: `PK`, `SK` o `studentId`.            |
| `KeyType=HASH`             | Partition Key      | Define cómo se distribuyen los datos físicamente. | Es obligatorio para cualquier tabla.          |
| `--attribute-definitions`  | Tipos de Atributos | Declaración del formato de los atributos clave.   | Solo se definen los campos de índices/llaves. |
| `AttributeType=S`          | Tipo de Dato       | `S`: String (Texto).                              | Otros: `N` (Número), `B` (Binario).           |
| `--provisioned-throughput` | Rendimiento        | Capacidad reservada de lectura/escritura.         | Determina costo y velocidad.                  |
| `ReadCapacityUnits`        | RCU                | Unidades de lectura.                              | 1 RCU = 1 lectura de 4 KB/seg.                |
| `WriteCapacityUnits`       | WCU                | Unidades de escritura.                            | 1 WCU = 1 escritura de 1 KB/seg.              |

#### 🧙 1.2. Usar el Asistente Interactiva

Si prefieres una guía paso a paso, AWS CLI ofrece un asistente:

```sh
aws dynamodb wizard new-table
```

#### 📋 1.3. Listar y Eliminar

Comandos rápidos para administración:

```sh
# Listar todas las tablas en la región actual
aws dynamodb list-tables

# Borrar una tabla específica
aws dynamodb delete-table --table-name Characters
```

---

### 📥 2. Operaciones con Datos

#### 📑 2.1. Carga Masiva desde JSON

Puedes insertar múltiples registros a la vez utilizando un archivo JSON:

```sh
aws dynamodb batch-write-item --request-items file://personajes.json
```

#### 🎵 2.2. Agregar Canciones (Batch Write)

Una vez creada la tabla de música, carga las canciones iniciales:

```sh
aws dynamodb batch-write-item --request-items file://songs.json
```

> **💡 Tip:** Asegúrate de que el formato del JSON coincida con la estructura requerida por DynamoDB (`PutRequest`).

---

### 🔍 3. Índices Secundarios Locales (LSI)

Los LSI te permiten realizar consultas utilizando una clave de orden diferente a la de la tabla principal, pero compartiendo la misma clave de partición.

#### 📁 3.1. Configuración de LSI (JSON)

Ejemplo de configuración para un índice en una tabla de música:

```json
[
  {
    "IndexName": "AlbumTitleIndex",
    "KeySchema": [
      { "AttributeName": "Artist", "KeyType": "HASH" },
      { "AttributeName": "AlbumTitle", "KeyType": "RANGE" }
    ],
    "Projection": {
      "ProjectionType": "INCLUDE",
      "NonKeyAttributes": ["Genre", "Year"]
    }
  }
]
```

#### 🏗️ 3.2. Crear Tabla con LSI

Para incluir el LSI al crear la tabla, usa el parámetro `--local-secondary-indexes`:

```sh
aws dynamodb create-table \
    --table-name MusicCollection \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
        AttributeName=AlbumTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --local-secondary-indexes file://lsi_config.json \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5
```

---

## 🐍 Uso con el SDK de Python (Boto3)

_Esta sección se puede expandir próximamente con ejemplos de código Python._

---
