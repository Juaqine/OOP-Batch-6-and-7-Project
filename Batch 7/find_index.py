#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

text = input("Enter your text: ")
char = input("Enter the character to find: ")

for i in range(len(text)):
    if text[i] == char:
        print(i)
        break
