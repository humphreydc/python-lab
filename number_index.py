number_DC =[]
positive_DC = 0
negative_DC = 0

while True:
    number_get = int(input("Enter an integer (0 to stop): "))

    if number_get == 0:
        break

    number_DC.append(number_get)

    if number_get > 0:
        positive_DC += 1
    elif number_get < 0:
        negative_DC += 1

    max_DC = max(number_DC)
    min_DC = min(number_DC)
    

print(f"Positive numbers: {positive_DC}")
print(f"Negative numbers: {negative_DC}")
print(f"Zeroes: 1 (terminated)")
print(f"Largest number: {max_DC}")
print(f"Smallest number: {min_DC}")