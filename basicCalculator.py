number1 = int(input("Enter your first number: "))
operator = input("Select your operator(+, -, *, /): ")
number2 = int(input("Enter your second number: "))


if operator == "+":
    result = (number1 + number2)
    print(f"Result: {result}")

elif operator == "-":
    print(f"Result: {number1} - {number2}")
elif operator == "*":
    print(f"Result: {number1} * {number2}")
elif operator == "/":
    print(f"Result: {number1} / {number2}")
else:
    print("Enter valid operator")
