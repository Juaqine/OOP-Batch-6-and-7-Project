#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#Ask the user for input
#Add the amount of spaces
#Print output

text = input("Enter text: ")
width = int(input("Enter the desired width: "))

result = ' ' * (width - len(text)) + text

print(result)
