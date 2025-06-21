from typing import List

def build_prompt(user_query: str, functions: List[str]) -> str:
    """
    Builds a prompt for the LLM including the user query and all available functions.
    Args:
        user_query (str): The user's natural language query.
        functions (List[str]): List of function signatures and docstrings.
    Returns:
        str: The formatted prompt string.
    """
    functions_str = '\n\n'.join(functions)
    prompt = f"""
Given the function library and a user query, output a JSON plan that lists the function calls required to fulfill the task. Each step should include:
- \"function\": function name
- \"args\": dictionary of arguments
- \"depends_on\": optional index of prior steps whose output is reused

User query: \"{user_query}\"

Function library:\n\n{functions_str}\n\nReturn the plan as a JSON list of steps.\n"""
    return prompt 