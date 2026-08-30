text = "Hello world"

vowel = 0
consonants = 0

for i in text.lower():
    if i in ("a", "e", "i", "o", "u"):
        vowel += 1
    elif i in " ":
        pass
    else:   
        consonants += 1

    

print(f"Vowels: {vowel}\nConsonants: {consonants}")
