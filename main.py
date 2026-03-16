import boto3
from boto3.dynamodb.conditions import Key
import json

if __name__ == "__main__":
    dynamodb_client = boto3.client("dynamodb")
    dynamodb_resource = boto3.resource("dynamodb")

    # 0. Lista todas las tablas de DynamoDB en la cuenta/región actual
    response = dynamodb_client.list_tables()
    print("📋 DynamoDB tables:")
    for name in response.get("TableNames", []):
        print("  📄", name)

    characters_table = dynamodb_resource.Table("Characters")

    # 1. Consulta un ítem específico utilizando su clave primaria
    response = characters_table.query(
        KeyConditionExpression=Key("PK").eq("character#43")
    )
    print("🔎 Query succeeded:")
    print(json.dumps(response["Items"], indent=2, default=str))

    # 2. Inserta o actualiza un ítem en la tabla
    characters_table.put_item(
        Item={
            "PK": "character#123",
            "Name": "Bird Person",
            "Gender": "Male",
            "Origin": "Earth (C-137)",
            "Species": ["Bird-Person"],
            "Location": [
                "Citadel of Ricks",
                "https://rickandmortyapi.com/api/location/3",
            ],
            "Status": "Alive",
            "Type": "Humanoid",
        }
    )
    print("✅ Item inserted successfully.")
    response = characters_table.get_item(Key={"PK": "character#123"})
    print("📦 Get item succeeded:")
    print(json.dumps(response["Item"], indent=2, default=str))
