import json
import jsonlines

def is_valid_jsonl(jsonl_string: str) -> bool:
    """
    Validates if a given multiline string is a valid JSON Lines (jsonl) format.

    A JSON Lines file is a text file where each line is a valid JSON object.
    This function checks if each line in the provided string can be parsed as JSON.

    Args:
        jsonl_string: A string containing the content to validate, where each
                      line is expected to be a JSON object.

    Returns:
        True if the string is a valid JSON Lines format, False otherwise.
    """
    if not jsonl_string.strip():
        return True  # An empty string or string with only whitespace is considered valid JSONL

    try:
        for line in jsonl_string.splitlines():
            if line.strip():  # Ignore empty lines
                json.loads(line)
        return True
    except json.JSONDecodeError:
        return False
    except Exception:
        # Catch any other unexpected errors during processing
        return False