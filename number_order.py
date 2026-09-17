first_number = int(input("Enter first number (a): "))
second_number = int(input("Enter second number (b): "))
third_number = int(input("Enter third number (c): "))

if first_number == second_number and second_number == third_number:
    print("All numbers are identical.")
elif first_number == second_number or second_number == third_number or first_number == third_number:
    print("Some numbers are equal.")
else:
    print("All numbers are distinct.")

if first_number >= second_number and first_number >= third_number:
    maximum = first_number
elif second_number >= first_number and second_number >= third_number:
    maximum = second_number
else:
    maximum = third_number

print(f"Maximum value is: {maximum}")
