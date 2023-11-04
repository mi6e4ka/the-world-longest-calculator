num1 = int(input("first number: "))
operation = input("operation (+, -, *, /): ")
num2 = int(input("second number: "))
result = 0

if operation == "+":
    if num1 == 1 and num2 == 1:
        result = 2
    ...
if operation == "-":
    if num1 == 1 and num2 == 1:
        result = 0
    ...
if operation == "*":
    if num1 == 1 and num2 == 1:
        result = 1
    ...
if operation == "/":
    if num1 == 1 and num2 == 1:
        result = 1
    ...
print(f"{num1} {operation} {num2} = {result}")