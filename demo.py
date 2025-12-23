def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("choose an operation:")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter the number of the operation you want to perform: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == "1":
    print("Result:", add(num1,num2))
elif operation == "2":
    print("Result:", subtract(num1, num2))
elif operation == "3":
    print("Result:", multipy(num1, num2))
elif operation == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
