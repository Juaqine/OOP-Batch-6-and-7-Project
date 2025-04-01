#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

text = input("Enter text: ")

lower_text = "".join(chr(ord(c) + 32)
    if 'A' <= c <= 'Z'
    else c for c in text)
