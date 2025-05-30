# simple-Passwprd-Generator
A simple yet secure Python script to generate random passwords with optional symbols and uppercase letters, along with checks to verify password content.

This Python project is a simple yet secure password generator that I built to practice writing functional code while learning about cryptographic safety, conditional logic, and modularity.

What I Built

• A function to generate random passwords of customizable length.

• Options to include:

• Symbols (!@#$...)

• Uppercase letters (A-Z)

Utility functions to:

• Check if the password contains uppercase characters

• Check if the password contains symbols

Key Concepts & Tools Used:

• string module → used to access character sets like lowercase letters, digits, and symbols.

• secrets module → used instead of random for secure password generation.

• Functions and conditionals to modularize and control password generation logic.

• For-loops to build passwords character-by-character.

• Boolean logic to return validation results.

What U can Learn :

• The difference between random vs secrets in security-sensitive code.

• How to slice and combine strings effectively for custom character pools

• How to build and use utility functions (contains_upper, contains_symbols)

• How to write a self-checking program (functions that verify password content)

• How to properly indent and debug Python code to avoid runtime errors

• Importance of writing clean, readable code that can be extended in the future

• How to combine multiple character sets based on user preferences.

• Writing and organizing code with clear logic and reusability.

• Basic input validation, code readability, and debugging.

## SAMPLE OUTPUT:
# 1 -> qy85y4q0r1 (U: False, s: False)
# 2 -> 9i57qz40u0 (U: False, s: False)
# ...


