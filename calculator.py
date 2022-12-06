#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Nov.30, 2022
# This program is a calculator that calculates the users nums using different signs that the user enters


def Calculator(num1_user, num2_user, sign):

    # Switch case to determine what sign to use
    match sign:
        case "+":
            return num1_user + num2_user
        case "-":
            return num1_user - num2_user
        case "*":
            return num1_user * num2_user
        case "/":
            return num1_user / num2_user
        case "%":
            return num1_user % num2_user
        case _:
            return -1


def main():
    # Gets num1 from the user
    num1_str = input("Enter a number: ")

    # Gets num2 from the user
    num2_str = input("\nEnter a second number: ")

    # Tries casting the numbers to float
    try:
        num1_user = float(num1_str)
        num2_user = float(num2_str)
    except:
        print("You must enter a number for both inputs.")
    else:
        # Gets the sign from the user
        sign_user = input("Enter an sign (signs: +, -, *, /, %): ")

        # set the result to the function to get the return value and calls the function
        result = Calculator(num1_user, num2_user, sign_user)

        # If the user entered a invalid sign
        if result == -1:
            print(f"\n{sign_user} is not a valid sign.")

        else:
            # Displays the result of the product
            print(f"\n{num1_user} {sign_user} {num2_user} = {result}")


if __name__ == "__main__":
    main()
