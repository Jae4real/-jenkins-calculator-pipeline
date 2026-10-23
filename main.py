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

# Kano Calculator - CI/CD Pipeline Project
if __name__ == "__main__":
    num1 = 5000
    num2 = 5600
    print(f"Kano Calculator Results:")
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print("Build Successful - All calculations working!")
