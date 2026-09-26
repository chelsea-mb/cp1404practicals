import random
low_number = int(input("Low number: "))
high_number = int(input("High number: "))

while high_number <= low_number:
    print("Please consult a dictionary for the definitions of 'lower' and 'higher'.")
    high_number = int(input("High number: "))
random_number = random.randint(low_number, high_number)
print(random_number)
print("🫠" * random_number)