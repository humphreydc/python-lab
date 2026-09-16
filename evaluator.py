student_score = float(input("Enter student score: "))
points_needed = 50 - student_score 

if student_score < 50:
    print(f"Result: FAIL. Needed {round(points_needed, 2)} more points.")
else:
    print("Congrats you have PASSED.")