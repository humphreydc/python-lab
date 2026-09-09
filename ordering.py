print("==========> Order Fast Food <==========")
hamburger = float(input("Enter number of hamburgers: "))
fries = float(input("Enter number of fries: "))
drink = float(input("Enter number of drinks: "))

total_hamburgers = hamburger * 2.00
total_fries = fries * 1.50
total_drinks = drink * 1.00

total_order = total_hamburgers + total_fries + total_drinks

print(f"Your total order cost {total_order:.2f} have a nice day!")