with open("calc.py", "w") as f:
    f.write("")
operators = ["+", "-", "*", "/"]
min_number = -1000
max_number = 1000
tab = " "*4
with open("calc.py", "a") as f:
    f.write(
f"""print("Welcome to world longest python calculator!")
print("Support number from {min_number} to {max_number}")
print("By mi6e4ka, enjoy!")
num1 = int(input("first number: "))
operation = input("operation (+, -, *, /): ")
num2 = int(input("second number: "))
result = 0
if not operation in ["+", "-", "*", "/"]:
    exit("wrong operator")
if num1 > {max_number} or num1 < {min_number}:
    exit("wrong first number (support only from {min_number} to {max_number})")
if num2 > {max_number} or num2 < {min_number}:
    exit("wrong second number (support only from {min_number} to {max_number})")\n""")
    for op in operators:
        f.write(f"if operation == \"{op}\":\n")
        for first in range(min_number, max_number+1):
            for second in range(min_number, max_number+1):
                f.write(f"{tab}if num1 == {first} and num2 == {second}:\n")
                f.write(f"{tab*2}result = {first} {op} {second}\n")
    f.write('print(f"{num1} {operation} {num2} = {result}")')