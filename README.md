[![PyPI version](https://badge.fury.io/py/jsonl_validator.svg)](https://badge.fury.io/py/jsonl_validator)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/jsonl_validator)](https://pepy.tech/project/jsonl_validator)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# jsonl_validator

A lightweight Python package to validate if a given string adheres to the JSON Lines (jsonl) format.

## Installation

To install `jsonl_validator`, use pip:

```bash
pip install jsonl_validator
```

## Usage

The `jsonl_validator` package provides a single function, `is_valid_jsonl`, which takes a multiline string and returns `True` if it's valid JSON Lines, and `False` otherwise.

### Example

```python
from jsonl_validator import is_valid_jsonl

valid_jsonl_string = """
{"name": "Alice", "age": 30}
{"name": "Bob", "city": "New York"}
{"id": 123, "data": [1, 2, 3]}
"""

invalid_jsonl_string = """
{"name": "Alice", "age": 30}
{"name": "Bob", "city": "New York"
{"id": 123, "data": [1, 2, 3]}
"""

print(f"Is the first string valid JSONL? {is_valid_jsonl(valid_jsonl_string)}")
# Output: Is the first string valid JSONL? True

print(f"Is the second string valid JSONL? {is_valid_jsonl(invalid_jsonl_string)}")
# Output: Is the second string valid JSONL? False

empty_string = ""
print(f"Is an empty string valid JSONL? {is_valid_jsonl(empty_string)}")
# Output: Is an empty string valid JSONL? True
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/jsonl_validator/issues).

## Author

**Eugene Evstafev**
* LinkedIn: [Eugene Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/)
* Email: hi@eugene.plus

## License

`jsonl_validator` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).