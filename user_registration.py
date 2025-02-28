import re

def validate_first_name(first_name):
    """
    Validates the first name:
    - Starts with a capital letter.
    - Has at least 3 characters.
    - Does not contain numbers.
    """
    pattern = r"^[A-Z][a-zA-Z ]{2,}$"
    if re.fullmatch(pattern, first_name) and not any(char.isdigit() for char in first_name):
        return True
    return False

def validate_last_name(last_name):
    """
    Validates the last name same rules as first name.
    """
    # Reusing logic to follow DRY principle
    return validate_first_name(last_name)  

def validate_email(email):
    """
    Validates email format:
    """
    pattern = r"^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def main():
    """
    Main function to take user input and validate first name, last name, and email.
    """
    while True:  # Validate first name
        first_name = input("Enter your first name: ").strip()
        if validate_first_name(first_name):
            break
        print("Invalid first name! It must start with a capital letter, be at least 3 characters long, and contain no numbers.")

    while True:  # Validate last name
        last_name = input("Enter your last name: ").strip()
        if validate_last_name(last_name):
            break
        print("Invalid last name! It must follow the same rules as the first name.")

    while True:  # Validate email
        email = input("Enter your email: ").strip()
        if validate_email(email):
            break
        print("Invalid email! Example: abc.xyz@bl.co.in")

    print("\nRegistration Successful!")
    print(f"Full Name: {first_name} {last_name}")
    print(f"Email: {email}\n")
    exit()

# Run the main function
if __name__ == "__main__":
    main()
