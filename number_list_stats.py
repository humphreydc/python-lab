print("=== NUMBER CALCULATOR ===")
number_store = []

for i in range(1, 6):
    number = float(input(f"Enter number {i}: "))
    number_store.append(number)

total_sum = sum(number_store)
highest_number = max(number_store)
lowest_number = min(number_store)

print(f"""
\n--- Results ---
"Numbers entered: {number_store}
Total Sum: {total_sum}
Highest Number: {highest_number}
Lowest Number: {lowest_number}
""")