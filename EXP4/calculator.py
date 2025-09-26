# calculator.py - Refactored Calculator

def get_input():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    return num1, operator, num2

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return "Error! Division by zero." if num2 == 0 else num1 / num2
    else:
        return "Invalid operator."

def main():
    num1, operator, num2 = get_input()
    result = calculate(num1, operator, num2)
    print("Result:", result)

if __name__ == "__main__":
    main()
