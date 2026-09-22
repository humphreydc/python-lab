initial_population = int(input("Enter initial population: "))
target_population = int(input("Enter target population: "))

current_population = initial_population
year = 0

while current_population < target_population :
    year += 1
    current_population *= 2
    print(f"Year {year}: Population = {current_population} ")

print(f"Target population reached in {year} year(s)!") 
