# Python simple calculator

operator = input("Enter an operator (+ - * /): ")

try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 1))

    elif operator == "-":
        result = num1 - num2
        print(round(result, 1))

    elif operator == "*":
        result = num1 * num2
        print(round(result, 1))

    elif operator == "/":
        result = num1 / num2
        print(round(result, 1))

    else:
        print("That's not a valid input.")

except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
