def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
print("Multiplication:", multiply(20, 10))
print("Division:", divide(20, 10))