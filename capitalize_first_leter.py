#rog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

text = input("Enter text: ")

if text:
    first_char = text[0]  # Get the first character
    rest = text[1:]
