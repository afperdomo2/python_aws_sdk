def dynamodb_events(event, context):
    try:
        for record in event["Records"]:
            if record["eventName"] == "MODIFY":
                manejar_update(record)
            elif record["eventName"] == "INSERT":
                manejar_insert(record)
            elif record["eventName"] == "REMOVE":
                manejar_remove(record)

    except Exception as e:
        print("❌ Error processing event:", e)
        raise e

    return "✅ Event processed successfully."


def manejar_update(record):
    print("🔄 Update event detected:")
    print(record)


def manejar_insert(record):
    print("➕ Insert event detected:")
    print(record)


def manejar_remove(record):
    print("➖ Remove event detected:")
    print(record)
