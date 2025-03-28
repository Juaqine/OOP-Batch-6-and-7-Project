#rog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

text = input("Enter text: ")

if text:
    first_char = text[0]  # Get the first character
    rest = text[1:]

if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)

new_text = first_char + "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in rest)

print("Output:", new_text)
else:
    print("Output: (empty string)")
