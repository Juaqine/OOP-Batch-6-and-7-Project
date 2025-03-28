#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

text = input("Enter text: ")

uppercase_text = ""
for char in text:
  if 'a' <= char <= 'z':
    uppercase_text += chr(ord(char) - 32)
    
