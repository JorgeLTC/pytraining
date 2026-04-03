a = input("Enter the first number: ")
b = input("Enter the second number: ")
operador = input("Enter the operator (+, -, *, /): ")
result = 0
if operador == "+":
    result = int(a) + int(b)
elif operador == "-":
    result = int(a) - int(b)
elif operador == "*":
    result = int(a) * int(b)
elif operador == "/":
    result = int(a) / int(b)
print(result)
