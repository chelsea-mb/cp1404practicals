def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    minimum_length = 10
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password must meet minimum length of ten characters.")
        password = input("Enter password: ")
    return password


main()
