#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter text: ")

words = text.split()

new_words = []
for word in words:
    if word:
        first_char = word[0] 
        rest = word[1:]
        
        if 'a' <= first_char <= 'z':
            first_char = chr(ord(first_char) - 32)
            
        new_word = first_char + "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in rest)
        new_words.append(new_word)

title_case_text = " ".join(new_words)
