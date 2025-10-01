String Number Adder
This project provides a Python function to calculate the sum of all positive numbers in a string input. Numbers can be separated by any non-numeric delimiters (commas, spaces, etc.). Negative numbers are not allowed and will raise an exception.

Features
Accepts a string containing numbers separated by any delimiter.

Ignores delimiters automatically.

Raises an exception when negative numbers are found.

Returns the sum as an integer.

Example
python
from test import add

result = add("1,2,3,6")
print(result)  # Output: 12
Handling Negatives
python
try:
    result = add("1,-2,3")
except ValueError as e:
    print(e)  # Output: Negatives not allowed: -2
Project Structure
text
.
├── test.py     # Main implementation
└── README.md    # Documentation
Function Definition
python
def add(args: str) -> int:
    """
    Calculate the sum of all positive numbers in a string.

    Args:
        args (str): A string containing numbers separated by any non-numeric delimiter.
                    Negative numbers are not allowed and will raise an exception.

    Returns:
        int: The sum of the numbers.
    """
Running the Script
bash
python main.py
Example output:

text
The result is: 12
