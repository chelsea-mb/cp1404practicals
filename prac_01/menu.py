"""
Use this pattern to create a very simple menu-driven program according to the pseudocode below:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input(" Your name: ")
choice = input("Choice: ")
while choice != "q":
    if choice == "h":
        print("Hello")
    if choice == "g":
        print("Goodbye")
    else:
        print("Invalid choice")
