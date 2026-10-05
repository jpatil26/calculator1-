def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def power(a,b):
    return a**b


print("===== SIMPLE CALCULATOR =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:")
print("Addition       :", add(a, b))
print("Subtraction    :", subtract(a, b))
print("Multiplication :", multiply(a, b))
print("Division       :", divide(a, b))
print("Power       :", power(a, b))