#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

text = input("Enter text: ")

lowercase_text = ""
for char in text:
  if 'A' <= char <= 'Z':
    lowercase_text += chr(ord(char) + 32)
  else:
    lowercase_text += char

print("Output:", lowercase_text)
