import requests
from typing import List, Dict
from prompt_builder import build_prompt
import json
import inspect
import functions_library

def get_function_signatures() -> List[str]:
    """
    Returns a list of all function signatures and docstrings from the function library.
    """
    signatures = []
    for name, func in inspect.getmembers(functions_library, inspect.isfunction):
        if func.__module__ == functions_library.__name__:
            sig = f"def {name}{inspect.signature(func)}:"
            doc = inspect.getdoc(func) or ""
            signatures.append(f"{sig}\n    \"\"\"{doc}\"\"\"")
    return signatures

def ask_ollama(prompt: str, model: str = "phi3:mini") -> str:
    """
    Sends a prompt to the Ollama API and returns the response.
    """
    url = "http://localhost:11434/api/generate"
    try:
        response = requests.post(url, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Could not connect to Ollama. Please ensure Ollama is running by executing 'ollama serve' in your terminal.")
    except Exception as e:
        raise e

def plan_pipeline(user_query: str) -> List[Dict]:
    """
    Generates a plan (sequence of function calls) for the user query using Ollama.
    """
    functions = get_function_signatures()
    prompt = build_prompt(user_query, functions)
    response = ask_ollama(prompt)

    # Extract JSON from the model's response, which might include extra text.
    try:
        json_start = response.find('[')
        json_end = response.rfind(']') + 1
        if json_start == -1 or json_end == 0:
            raise ValueError("No JSON array found in the model's response.")
        
        plan_str = response[json_start:json_end]
        plan_json = json.loads(plan_str)
    except Exception as e:
        raise ValueError(f"Failed to parse plan JSON: {e}\nRaw Response:\n{response}")
    
    return plan_json 