text = input("Enter a sentence: ")
letter = input("Enter target character to search: ")

count = 0

for char in text.lower():
    if char == letter.lower():
        count += 1
    
if count > 0:
    print(f"The character '{letter}' appeared {count} time(s) in the sentence.")
else:
    print(f"The character '{letter}' was not found in the sentence.")