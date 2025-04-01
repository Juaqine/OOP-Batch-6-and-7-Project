#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

text = input("Enter text: ")

lower = all('a' <= c <= 'z' for c in text if c.isalpha())

print(f"Is lowercase: {lower}")
