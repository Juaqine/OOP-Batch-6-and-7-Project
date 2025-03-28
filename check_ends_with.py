#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#Ask the user for input
#Check if text ends with suffix
#If suffix longer than text it can't match
#Else compare the end of the text with suffix
#Print output

text = input("Enter text: ")
suffix = input("Enter suffix to check: ")

if len(suffix) > len(text):
  result = f'The text does NOT end with "{suffix}".'
else:
  if text[-len(suffix):] == suffix:
    result = f'The text ENDS with "{suffix}".'
  else:
    result = f'The text does NOT end with "{suffix}".'

print("Output:", result)
