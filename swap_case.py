#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
#Ask user for input
#Swap the case
#If uppercase, convert to lowercase
#If lowercase, convert to uppercase
#Else keep unchanged
#Print output

text = input("Enter text: ")

swapped_text = ""
for char in text:
    if 'A' <= char <= 'Z':
        swapped_text += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        swapped_text += chr(ord(char) - 32)
    else:
        swapped_text += char

print("Output:", swapped_text)
