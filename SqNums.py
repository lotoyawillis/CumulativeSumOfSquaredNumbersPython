"""

Name:Lotoya Willis
Date:08/29/2024
Assignment:1
Due Date:09/01/2024
About this project:prompts the user to input a positive numeric value, displays all
the square numbers up to that value, and calculates the sum of the square numbers
Assumptions:N/A
All work below was performed by Lotoya Willis

"""


# Calculates the sum of all elements in the list and returns the total
def sum_of_squares(li):
    total = 0
    for i in li:
        total = total + int(li[li.index(i)])
    return total


# Calculates the squares up to the user-inputted value, appends them to a list,
# prints the element, and returns the list
def calculate_squares(lim):
    i = 2
    element = i ** 2
    li = []
    while element < lim:
        li.append(element)
        print(element)
        i = i + 1
        element = i ** 2
    return li


# Ensures the user's input is a valid number before moving forward and returns the
# value
def validate_input():
    try:
        num = int(input(" please enter in a number >"))
    except ValueError:
        num = -1
    while num < 0:
        num = validate_input()
    return num


# Main function
# Calls functions and displays final sum in a formatted string
def main():
    limit = validate_input()
    li = calculate_squares(limit)
    num = sum_of_squares(li)
    print(f"The cumulative sum of the square numbers is   {num}  .")

    return 0


if __name__ == "__main__":
    main()
