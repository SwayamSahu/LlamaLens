import os
from typing import List, Dict, Any
import requests

USE_CEREBRAS = os.environ.get("USE_CEREBRAS", "1") == "1"
DEFAULT_MODEL = os.environ.get("LLAMA_MODEL", "llama-4-scout-17b-16e-instruct")

def call_llama(messages: List[Dict[str, str]], max_tokens: int = 512, temperature: float = 0.2):
    if USE_CEREBRAS:
        from cerebras.cloud.sdk import Cerebras
        client = Cerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))
        stream = client.chat.completions.create(
            messages=messages,
            model=DEFAULT_MODEL,
            stream=True,
            max_completion_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
        )
        output = []
        for chunk in stream:
            delta = getattr(chunk.choices[0].delta, "content", None)
            if delta:
                output.append(delta)
        return {"text": "".join(output)}
    else:
        raise ValueError("Only Cerebras mode is currently supported in this build.")


def extract_text_from_response(resp: Dict[str, Any]) -> str:
    if "text" in resp:
        return resp["text"]
    if "choices" in resp and resp["choices"]:
        choice = resp["choices"][0]
        if "message" in choice and "content" in choice["message"]:
            return choice["message"]["content"]
    return str(resp)
