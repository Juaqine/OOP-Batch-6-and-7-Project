#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

#Ask the user for input
#Find non-space character
#Print output

text = input("Enter text: ")

i = len(text) - 1
while i >= 0 and text[i] == ' ':
    i -= 1

print(f"Original: '{text}'")
print(f"Trimmed: '{text[:i+1]}'")
