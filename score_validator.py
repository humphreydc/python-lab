while True:
    score = float(input("Enter exam score (0-100): "))

    if 0 <= score <= 100:
        print(f"Valid score recorded: {score}")
        break
    else:
        print("Invalid Score! Please enter a value between 0 and 100.")