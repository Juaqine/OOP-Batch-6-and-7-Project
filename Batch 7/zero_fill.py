#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

text = input("Enter text: ")
width = int(input("Enter the desired width: "))

print('0' * (width - len(text)) + text)
