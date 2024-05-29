"""
@file main.py
@brief This file contains the calculator function which performs basic arithmetic operations.
"""

def calculator(a, b, c):
    """
    @brief Performs basic arithmetic operations.
    @param a First operand.
    @param b Second operand.
    @param c Operator (either '+' for addition or '-' for subtraction).
    @return Result of the arithmetic operation.
    """
    if c == '+':
        return a + b
    if c == '-':
        return a - b

# Example usage of the calculator function
print(calculator(2, 3, '+'))  # Output: 5