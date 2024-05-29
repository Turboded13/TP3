"""
@file main.py
@brief This file contains functions for basic arithmetic operations.
"""

def add(a, b):
    """
    @brief Adds two numbers.
    @param a First number.
    @param b Second number.
    @return Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    @brief Subtracts second number from first number.
    @param a First number.
    @param b Second number.
    @return Difference between a and b.
    """
    return a - b

if __name__ == "__main__":
    print(add(2, 3))       # Output: 5
    print(subtract(5, 2))  # Output: 3
