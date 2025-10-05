import json

def format_json(data: str) -> str:
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=2)
    except Exception:
        return data
