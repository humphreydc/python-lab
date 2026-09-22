current_fuel = 50.0
print(f"Current fuel: {current_fuel} liters")

while current_fuel > 0:
    fuel_used = float(input("Enter fuel used on this leg (liters): "))
    current_fuel -= fuel_used
    
    if current_fuel > 0:
        print(f"Remaining fuel: {current_fuel}\n")

print("Fuel empty! Refueling required")