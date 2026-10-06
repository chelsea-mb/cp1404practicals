"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

We need a list to store the incomes.
How do you add values to a list?

We need a counter variable (int) for the month number.
Remember that list indexes start at 0, but we want to print from 1.

How many loops will we need? What kind of loops?

We need a cumulative total to update as we loop through the list to display the incomes.

And lastly we need to format the output nicely, which we can use f-strings for.
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = [] #List to store incomes
    months = int(input("How many months? "))

    for month in range(1, months + 1): #Month counter. First loop
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income) #add values to a list

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1): #Second loop
        income = incomes[month - 1]
        total += income #Cumulative total
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")



main()
