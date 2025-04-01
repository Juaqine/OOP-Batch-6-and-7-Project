#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#Ask the user for input
#Convert lowercase letters to uppercase
#If letter lowercase convert to uppercase
#Else keep letter uppercase
#Print output

text = input("Enter text: ")

uppercase_text = ""
for char in text:
  if 'a' <= char <= 'z':
    uppercase_text += chr(ord(char) - 32)
  else:
    uppercase_text += char

print("Output:", uppercase_text)
