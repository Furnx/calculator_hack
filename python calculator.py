from addition import add
from division import divide
from subtraction import subtraction


def main():
    print("Welcome to Calculator!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Chooose operation (+, -, *, /): ")

    if choice == '+':
        # Call the function from addition.py
        result = add(num1, num2)
    elif choice == '-':
        result = subtraction(num1, num2)
    
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()