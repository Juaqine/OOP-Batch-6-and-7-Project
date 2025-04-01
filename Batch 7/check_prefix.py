#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

#Ask the user for input
#Check if prefix matches
#Print output

text = input("Enter text: ")
prefix = input("Enter prefix to check: ")

if text[:len(prefix)] == prefix:
    print(f"The string starts with '{prefix}'.")
else:
    print(f"The string does not start with '{prefix}'.")
