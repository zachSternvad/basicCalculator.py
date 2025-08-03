try:
    number1 = int(input("Enter your first number: "))
except ValueError:
    print("\033[91mEnter a valid number\033[0m")
    exit()

operator = input("Select your operator(+, -, *, /): ")

try:
    number2 = int(input("Enter your second number: "))
except ValueError:
    print("\033[91mEnter a valid number\033[0m")
    exit()


if operator == "+":
    result = (number1 + number2)
    print(f"Result: {result}")

elif operator == "-":
    result = (number1 - number2)
    print(f"Result: {result}")

elif operator == "*":
    result = (number1 * number2)
    print(f"Result: {result}")

elif operator == "/":
    result = (number1 / number2)
    print(f"Result: {result}")

else:
    print("\033[91mEnter valid operator\033[0m")
