#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

text = input("Enter text: ")
char = input("Enter the character to count: ")

print(text.split(char).__len__() - 1)
