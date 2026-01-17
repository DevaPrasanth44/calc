import os
from calculator import add, subtract, multiply, divide

def main():
    # Get input from Jenkins parameters (environment variables)
    a = int(os.getenv("NUMBER1", 0))
    b = int(os.getenv("NUMBER2", 0))
    operation = os.getenv("OPERATION", "add")

    print("Calculator Result:")
    if operation == 'add':
        print(f"{a} + {b} = {add(a, b)}")
    elif operation == 'subtract':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif operation == 'multiply':
        print(f"{a} * {b} = {multiply(a, b)}")
    elif operation == 'divide':
        try:
            print(f"{a} / {b} = {divide(a, b)}")
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    main()
