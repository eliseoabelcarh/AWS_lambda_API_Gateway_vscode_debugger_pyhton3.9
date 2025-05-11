import json

def login(event: dict):
    success = False

    u_name = get_value_from_event(event, "user_name")
    password = get_value_from_event(event, "password")
    phrase = get_value_from_event(event, "pass_phrase")

    # simple test, todo connect to a db
    if u_name == "tony_stark" and password == "ironman2" and phrase == "I am Iron Man":
        success = True

    return success, u_name

def get_value_from_event(payload: dict, key):
    if "body" in payload:
        payload = payload["body"]

    if type(payload) is str:
        try:
            payload = str(payload).replace("'", "\"")
            payload = json.loads(payload)
        except Exception as e:
            # not the best way to log, but we're doing it this way for simplicity
            print(str(e))

    value = payload.get(key, None)
    return value

def lambda_handler(event, context):
    print(f'event: {event}')
    print(f'context: {context}')

    success, user_name = login(event)

    statusCode = 200
    if not success:
        statusCode = 403

    response = {
        'statusCode': statusCode,
        'body': {
            'message': f'hello {user_name} from lambda',
            'login_success': success
        }
    }

    return response
