fruit_store = []
print("=== FRUIT PRICE CHECKER === ")

for i in range(1, 4):
    fruit_name = input(f"\nEnter fruit {i} name: ")
    fruit_price = float(input(f"Enter price of {fruit_name}: "))
    
    fruit_store.append((fruit_name, fruit_price))

print("\n--- Summary ---")
total_cost = 0.0

for fruit, price in fruit_store:
    print(f"{fruit}: PHP {price}")
    total_cost += price

print(f"Total Cost: PHP {total_cost}")