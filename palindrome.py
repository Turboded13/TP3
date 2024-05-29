"""
@file palindrome.py
@brief This file contains functions to check if a string is a palindrome.
"""

def is_palindrome(s):
    """
    @brief Checks if the given string is a palindrome.
    @param s The string to check.
    @return True if the string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
print(is_palindrome("A man a plan a canal Panama"))  # Output: True!