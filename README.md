# 🐍 Python AWS SDK

Ejemplos y utilidades para trabajar con **AWS DynamoDB** y **AWS Lambda / API Gateway** usando **Python (Boto3)** y **AWS CLI**.

---

## 📁 ¿Qué hay en este proyecto?

| Archivo / carpeta                  | Descripción rápida                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| `ejercicios/1-dynamodb/main.py`    | Ejemplo principal que lista tablas, consulta un ítem, inserta un ítem y lo recupera de DynamoDB. |
| `create_table_wizard`              | Script AWS CLI para crear la tabla `Characters` (usada por `main.py`).                           |
| `create_table_music.sh`            | Script AWS CLI para crear la tabla `Music` con un LSI (`AlbumTitleIndex`).                       |
| `personajes.json`                  | Datos de ejemplo para carga masiva en DynamoDB.                                                  |
| `songs.json`                       | Datos de ejemplo para la tabla de música.                                                        |
| `lsi_config.json`                  | Configuración JSON para un índice secundario local (LSI).                                        |
| `api_gateway_lambda_template.json` | CloudFormation para crear una Lambda + API Gateway + IAM roles.                                  |
| `ejercicios/`                      | Ejercicios adicionales (DynamoDB, Lambda).                                                       |

---

## ✅ Requisitos previos

1. **Python 3.8+** (o equivalente).
2. **AWS CLI** configurado (credenciales + región):
   - `aws configure` o variables de entorno `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`.
3. **Dependencias Python**: `boto3`.

---

## 🛠️ Pasos iniciales (entorno virtual)

### 1) Crear el entorno virtual

```bash
python -m venv .venv
```

### 2) Activar el entorno virtual

#### 🪟 Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

#### 🍎 macOS / 🐧 Linux

```bash
source .venv/bin/activate
```

### 3) Instalar dependencias

```bash
pip install boto3
```

---

## ▶️ Ejecutar el ejemplo principal (`ejercicios/1-dynamodb/main.py`)

Este script hace lo siguiente:

1. Lista todas las tablas de DynamoDB en la cuenta/región.
2. Consulta un ítem en la tabla `Characters`.
3. Inserta/actualiza un ítem en `Characters`.
4. Recupera el ítem insertado.

```bash
python ejercicios/1-dynamodb/main.py
```

> ⚠️ Si utilizas Windows y no tienes `python` en tu PATH, usa `python3` o la ruta completa al ejecutable de tu entorno virtual (por ejemplo, `.\.venv\Scripts\python.exe`).

---

## 🔵 AWS CLI: crear y gestionar tablas

### Crear la tabla `Characters`

```bash
bash create_table_wizard
```

### Crear la tabla `Music` (incluye LSI)

```bash
bash create_table_music.sh
```

### Listar / eliminar tablas

```bash
aws dynamodb list-tables
aws dynamodb delete-table --table-name Characters
```

---

## 📥 Carga masiva de datos (batch-write)

```bash
aws dynamodb batch-write-item --request-items file://personajes.json
aws dynamodb batch-write-item --request-items file://songs.json
```

> ✅ Asegúrate de que la tabla exista antes de ejecutar estas cargas.

---

## ☁️ Plantilla CloudFormation (Lambda + API Gateway)

El archivo `api_gateway_lambda_template.json` crea:

- Una función **Lambda** con código inline que devuelve "Hola Mundo".
- Un rol **IAM** con permisos para ejecutar Lambda y acceso a DynamoDB.
- Un **API Gateway** con un endpoint `POST /insertar` que invoca la Lambda.
- Un rol para que **API Gateway** pueda enviar logs a CloudWatch.

---

## 🧪 Ejercicios adicionales

- `ejercicios/1-dynamodb/main.py`: otro ejemplo de uso de DynamoDB.
- `ejercicios/2-crear-lambda/`: recursos para crear una función Lambda.

---

¡Listo! Ahora la documentación refleja lo que hay en el proyecto y cómo usarlo. Si quieres, puedo agregar un pequeño apartado con el comportamiento exacto de `main.py` y cómo ajustar el nombre de la tabla o región.

---
