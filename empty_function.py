def displayGreeting(word):
    if word ==  "":
        print("Humayo kayo at magpakarami!")
    else:
        print("Magandang araw " + word + "!")

word = input("Enter your name: ")
displayGreeting(word)
