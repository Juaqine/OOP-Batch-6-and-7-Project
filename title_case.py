#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter text: ")

words = text.split()

new_words = []
for word in words:
    if word:
        first_char = word[0] 
        rest = word[1:]
