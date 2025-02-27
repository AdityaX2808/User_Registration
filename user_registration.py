import re

def first_name(name):
    return bool(re.fullmatch(r'^[A-Z][a-zA-Z]{2,}$', name))

def main():
    first_name = input("Enter your first name: ")

    if first_name(first_name):
        print("Valid first name!")
    else:
        print("Invalid name. First name must start with a capital letter and have at least 3 characters.")


if __name__ == "__main__":
    main()