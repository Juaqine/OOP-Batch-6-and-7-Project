#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter text: ")
char = input("Enter the character to find: ")

for i in range(len(text)-1, -1, -1):
 if text[i] == char:
        print(i)
        break
