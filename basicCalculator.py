number1 = int(input("Enter your first number: "))
operator = input("Select your operator(+, -, *, /): ")
number2 = int(input("Enter your second number: "))


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
    print("Enter valid operator")
