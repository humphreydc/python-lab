water_bill = float(input("Enter water usage in cubic meters: "))
total_text = "Total Water Bill:"

if water_bill <= 10:
    print(total_text, "$15.00")
elif water_bill >= 11 and water_bill <= 30:
    total_water_bill = water_bill * 1.5
    print(total_text, f"${total_water_bill}")
elif water_bill > 30:
    total_water_bill = water_bill * 2.5
    print(total_text, f"${total_water_bill}")
else:
    print("Water usage invalid!")