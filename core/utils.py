import base64
import urllib.parse
import random
import uuid
import json
import base64 as b64


def encode_base64(string):
    try:
        return base64.b64encode(str(string).encode()).decode()
    except Exception as e:
        return f"Error encoding: {e}"

def decode_base64(encoded_string):
    try:
        return base64.b64decode(encoded_string.encode()).decode()
    except Exception as e:
        return f"Error decoding: {e}"

def url_encode(string):
    try:
        return urllib.parse.quote_plus(str(string))
    except Exception as e:
        return f"Error encoding URL: {e}"

def url_decode(encoded_string):
    try:
        return urllib.parse.unquote_plus(encoded_string)
    except Exception as e:
        return f"Error decoding URL: {e}"

def random_user_agent():
    try:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 10)"
        ]
        return random.choice(user_agents)
    except Exception as e:
        return f"Error generating user-agent: {e}"

def decode_jwt(token):
    try:
        header, payload, signature = token.split('.')
        decoded_header = json.loads(b64.urlsafe_b64decode(header + '=='))
        decoded_payload = json.loads(b64.urlsafe_b64decode(payload + '=='))
        return {"header": decoded_header, "payload": decoded_payload}
    except Exception as e:
        return f"Error decoding JWT: {e}"

def generate_uuid():
    try:
        return str(uuid.uuid4())
    except Exception as e:
        return f"Error generating UUID: {e}"
