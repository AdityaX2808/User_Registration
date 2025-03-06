import re
import logging

# Set up logging configuration
logging.basicConfig(
    filename="user_registration.log",  # Save logs to a file
    filemode="w",
    level=logging.INFO,  # Log INFO and above (WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def validate_first_name(first_name):
    """
    Validates the first name:
    - Starts with a capital letter.
    - Has at least 3 characters.
    - Does not contain numbers.
    """
    pattern = r"^[A-Z][a-zA-Z ]{2,}$"
    if re.fullmatch(pattern, first_name) and not any(char.isdigit() for char in first_name):
        logging.info(f"Valid first name: {first_name}")
        return True
    
    logging.warning(f"Invalid first name attempt: {first_name}")
    return False

def validate_last_name(last_name):
    """
    Validates the last name (same rules as first name).
    """
    return validate_first_name(last_name)  

def validate_email(email):
    """
    Validates email format.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(pattern, email):
        logging.info(f"Valid email: {email}")
        return True
    
    logging.warning(f"Invalid email attempt: {email}")
    return False

def validate_mobile_number(number):
    """
    Validates the mobile number:
    - Should contain +91 in front.
    - Should be exactly 10 digits after +91.
    """
    pattern = r"^\+91\s[6-9]\d{9}$"
    if re.fullmatch(pattern, number):
        logging.info(f"Valid mobile number: {number}")
        return True

    logging.warning(f"Invalid mobile number attempt: {number}")
    return False

def validate_password(password):
    """
    Validates password:
    - At least 8 characters long.
    - At least 1 uppercase character.
    - At least 1 number.
    - At least 1 special character.
    """
    special_chars = re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and len(special_chars) == 1
    ):
        logging.info("Valid password entered.")
        return True

    logging.warning("Invalid password attempt.")
    return False   

def main():
    """
    Main function to take user input and validate first name, last name, email, mobile number, and password.
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

    while True:  # Validate mobile number
        mobile_number = input("Enter your mobile number (Format: +91 1234567890): ").strip()
        if validate_mobile_number(mobile_number):
            break
        print("Invalid mobile number! It must follow the format: +91 1234567890")    

    while True:  # Validate password
        password = input("Enter your password: ").strip()
        if validate_password(password):
            break
        print("Invalid password! It must be at least 8 characters, contain 1 uppercase letter, 1 number, and 1 special character.")

    logging.info("Registration successful!")
    
    print("\nRegistration Successful!")
    print(f"Full Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Mobile Number: {mobile_number}")
    print(f"Password: {password}")

if __name__ == "__main__":
    main()
