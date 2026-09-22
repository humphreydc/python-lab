while True:
    print("=== GRADE TOOL MENU ===")
    print("1. Compute Passed/Failed Status")
    print("2. Display Grading Rubic")
    print("3. Exit Program\n")

    choice = input("Select option (1-3): ")

    if choice == "1":
        print("Status: Minimum passing score is 75%.")
        input("\nPress Enter to return to the main menu...")
    elif choice == "2":
        print("Grade: 10% Attendance, 50% Performance Task, 40% Exams.")
        input("\nPress Enter to return to the main menu...")
    elif choice == "3":
        print("Exiting Grade Tool...")
        break
    else:
        print("Please enter a valid option!")