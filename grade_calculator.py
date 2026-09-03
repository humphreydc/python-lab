attendance_grade = float(input("Enter Attendance Grade: "))
midterm_grade = float(input("Enter Attendance Grade: "))
pre_final_grade = float(input("Enter Attendance Grade: "))


final_grade = (attendance_grade * 0.10) + (midterm_grade * 0.40) + (pre_final_grade * 0.50)

print(f"Final Grade: {final_grade:.1f}")