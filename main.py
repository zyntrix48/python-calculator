from modules.calculator import *


def show_operators(operators):
    for i, operator in enumerate(operators):
        print(f"{i + 1}.", operator)

def main():
    try:
        operators = ["+", "-", "*", "/"]

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        show_operators(operators)
        operator = int(input("Enter operator(enter index): "))

        match operator:
            case 1:
                print(add(a, b))
            case 2:
                print(sub(a, b))
            case 3:
                print(mult(a, b))
            case 4:
                print(div(a, b))
            case _:
                print("Unknow operator!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()