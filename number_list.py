number_DC =[]

while True:
    number_get = input("Enter a number (or 'done' to finish): ") 
    
    if number_get.lower() == 'done':
        break

    number_DC.append(float(number_get))

    if len(number_DC) > 0:
        sum_DC = sum(number_DC)
        avg_DC = sum_DC / len(number_DC)
        max_DC = max(number_DC)
        min_DC = min(number_DC)
    else:
        print("No numbers was entered")
    

print(f"Numbers entered: {number_DC}")
print(f"Sum of numbers: {sum_DC}")
print(f"Average of numbers: {avg_DC}")
print(f"Largest number: {max_DC}")
print(f"Smallest number: {min_DC}")