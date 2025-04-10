import math_utils

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    op = input("Choose a operator: ")

    operation = {'+': math_utils.add, '-': math_utils.subtract, '*': math_utils.multiply, '/': math_utils.divide, '^': math_utils.power, '%': math_utils.mod}

    if op in operation:
        try:
            f = operation[op](a, b)
            print(f)
        except Exception as e:
            print(e)
    else:
        print("Try again")

if __name__ == "__main__":
    main()
