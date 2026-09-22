minimum_length = 10
password = input("Enter password: ")
while len(password) < minimum_length:
    print("Password must meet minimum length of ten characters.")
    password = input("Enter password: ")
print("*" * len(password))
