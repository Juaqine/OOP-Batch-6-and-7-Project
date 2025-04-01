#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#Ask the user for input
#Check if text starts with prefix
#If yes remove prefix
#Print output

text = input("Enter text: ")
prefix = input("Enter prefix to remove: ")

if text.startswith(prefix):
  text = text[len(prefix):]

print("Output:", text)
