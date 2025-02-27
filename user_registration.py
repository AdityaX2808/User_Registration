import re

def first_name(name):
    return bool(re.fullmatch(r'^[A-Z][a-zA-Z]{2,}$', name))

def last_name(name):
    return bool(re.fullmatch(r'^[A-Z][a-zA-Z]{2,}$', name))

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if first_name(first_name) and last_name(last_name):
        print("Valid first and last name!")
    else:
        print("Invalid name. First and last names must start with a capital letter and have at least 3 characters.")


if __name__ == "__main__":
    main()