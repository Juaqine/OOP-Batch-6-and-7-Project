#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

text = input("Enter text: ")
suffix = input("Enter suffix to check: ")

if len(suffix) > len(text):
