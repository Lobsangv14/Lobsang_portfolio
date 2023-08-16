import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        raise ValueError("Invalid input for square root")

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def main():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Exit")

        choice = input("Enter choice (1-10): ")

        if choice == '10':
            print("Calculator exited.")
            break

        try:
            if choice in ['1', '2', '3', '4', '5']:
                numero1 = float(input("Enter first number: "))
                numero2 = float(input("Enter second number: "))
            elif choice in ['6', '7', '8', '9']:
                num = float(input("Enter a number: "))
            else:
                print("Invalid input")
                continue

            if choice == '1':
                print("Result:", add(numero1, numero2))
            elif choice == '2':
                print("Result:", subtract(numero1, numero2))
            elif choice == '3':
                print("Result:", multiply(numero1, numero2))
            elif choice == '4':
                print("Result:", divide(numero1, numero2))
            elif choice == '5':
                print("Result:", exponentiate(numero1, numero2))
            elif choice == '6':
                print("Result:", square_root(num))
            elif choice == '7':
                print("Result:", sine(num))
            elif choice == '8':
                print("Result:", cosine(num))
            elif choice == '9':
                print("Result:", tangent(num))

        except ValueError as e:
            print("Error:", e)
            continue

if __name__ == "__main__":
    main()