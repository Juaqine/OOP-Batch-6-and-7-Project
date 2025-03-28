#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

text = input("Enter text:")
space = int(input("Enter the total width: "))

if len(text) >= width:
    result = text
else:
    total_spaces = width - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    result = " " * left_spaces + text + " " * right_spaces

print("Output:", f'"{result}"')
