#ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

text = input("Enter text: ")
space = int(input("Enter the total width: "))

if len(text) >= width:
  result = text 
else:
  result = text + " " * (width - len(text))

print("Output:", f'"{result}"')
