import os
from calculator import add, subtract, multiply, divide

def main():
    a = int(os.getenv("NUMBER1", 0))
    b = int(os.getenv("NUMBER2", 0))
    operation = os.getenv("OPERATION", "add")

    if operation == 'add':
        print(f"{a} + {b} = {add(a, b)}")
    elif operation == 'subtract':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif operation == 'multiply':
        print(f"{a} * {b} = {multiply(a, b)}")
    elif operation == 'divide':
        print(f"{a} / {b} = {divide(a, b)}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
