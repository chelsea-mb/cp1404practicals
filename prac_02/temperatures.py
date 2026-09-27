"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""


def main():
    """Execute main function"""
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            result = celsius_to_fahrenheit()
            print(f"{result:.2f}F")
        elif choice == "F":
            result = fahrenheit_to_celsius()
            print(f"{result:.2f}C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit"""
    celsius = float(input("Enter degree/s in celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius"""
    fahrenheit = float(input("Enter degree/s in fahrenheit: "))
    celsius = (fahrenheit - 32) // 1.8
    return celsius


main()
