text = input("Enter text: ")
prefix = input("Enter prefix to remove: ")

if text.startswith(prefix):
  text = text[len(prefix):]

print("Output:", text)
