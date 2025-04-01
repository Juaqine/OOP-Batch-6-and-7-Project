#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

text = input("Enter text: ")

upper_text = "".join(chr(ord(c) - 32) 
  if 'a' <= c <= 'z' 
  else c for c in text)
