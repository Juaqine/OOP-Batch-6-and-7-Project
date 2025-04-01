#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#Ask the user for input
#Convert all lowercase to uppercase
#Print output

text = input("Enter text: ")

upper_text = "".join(chr(ord(c) - 32) 
  if 'a' <= c <= 'z' 
  else c for c in text)

print(f"Uppercase: '{upper_text}'")
