PI = 3.14
str = "Hello World!"
num = 7
is_allowed = False
is_active = True
items = ["Apple", "Banana", "Orange", "Sayote", "Watermelon", "Peach", "Kiwi", "Pomegranate"]

#if-else statement
if is_allowed:
  print(f"{str} & {num}")
else:
  print("You cannot pass!")

#for loop for items list
for item in items:
  print(item)

print("""
End of code...
continue with functions and classes
import too.
""")

states = ("Active", "Inactive", "Pending")

print(states)
print("These are the states of the program")

dit = {
  key: "yes",
  num: 4,
  check: False
}

print(dit)
print("This is the second half of the program.")

def compute():
  pass

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

print("Advance code concepts below here.")
