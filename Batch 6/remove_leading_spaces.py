#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#Ask the user for input
#Find the first non-space character
#Slice the string 
#Print output

text = input("Enter text: ")

index = 0
while index < len(text) and text[index] == " ":
  index +=1

trimmed_text = text[index:]

print("Output:", trimmed_text)
