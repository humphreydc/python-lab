password_error_DC = []

while True:
    password_get = input("Enter a password: ") 
    current_errors = []
    
    if len(password_get) < 8:
        current_errors.append("At least 8 characters long")
        
    if not any(char.isupper() for char in password_get):
        current_errors.append("At least one uppercase letter")
        
    if not any(char.islower() for char in password_get):
        current_errors.append("At least one lowercase letter")
        
    if not any(char.isdigit() for char in password_get):
        current_errors.append("At least one digit")
        
    if len(current_errors) == 0:
        print("Success: Your password is valid!")
        break
    else:
        print("Error! Your password is missing:")
        for error in current_errors:
            print(f" - {error}")
        password_error_DC.append(password_get) 
        print("Please try again.\n")