age = int(input("Enter applicant's age: "))

if age < 21:
    print("Loan Rejected: Applicant must be at least 21 years old")
else:
    income = float(input("Enter monthly income: "))
    credit_score = int(input("Enter credit score: "))

    if income >= 3000:
        if credit_score >= 700:
            print("Loan Approved: Low Risk Tier (Interest Rate: 4%)")
        elif credit_score >= 600:
            print("Loan Approved: Standard Tier (Interest Rate: 7%)")
        else:
            print("Loan Rejected: Low Credit Rating")
    else:
        has_guarantor = input("Is a valid guarantor available? (yes/no): ").lower() == "yes"

        if has_guarantor and credit_score >= 650:
            print("Loan Approved with Guarantor Sub-Tier")
        else:
            print("Loan Rejected: Insufficient Income and Credit Status")